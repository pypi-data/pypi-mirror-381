"""
Dramatically simplified PyQt parameter form manager.

This demonstrates how the widget implementation can be drastically simplified
by leveraging the comprehensive shared infrastructure we've built.
"""

import dataclasses
import logging
from typing import Any, Dict, Type, Optional, Callable, Tuple
from dataclasses import replace
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QLabel, QPushButton, QLineEdit, QCheckBox, QComboBox, QGroupBox
from PyQt6.QtCore import Qt, pyqtSignal

# Performance monitoring
from openhcs.utils.performance_monitor import timer, get_monitor

# SIMPLIFIED: Removed thread-local imports - dual-axis resolver handles context automatically
# Mathematical simplification: Shared dispatch tables to eliminate duplication
WIDGET_UPDATE_DISPATCH = [
    (QComboBox, 'update_combo_box'),
    ('get_selected_values', 'update_checkbox_group'),
    ('set_value', lambda w, v: w.set_value(v)),  # Handles NoneAwareCheckBox, NoneAwareIntEdit, etc.
    ('setValue', lambda w, v: w.setValue(v if v is not None else w.minimum())),  # CRITICAL FIX: Set to minimum for None values to enable placeholder
    ('setText', lambda w, v: v is not None and w.setText(str(v)) or (v is None and w.clear())),  # CRITICAL FIX: Handle None values by clearing
    ('set_path', lambda w, v: w.set_path(v)),  # EnhancedPathWidget support
]

WIDGET_GET_DISPATCH = [
    (QComboBox, lambda w: w.itemData(w.currentIndex()) if w.currentIndex() >= 0 else None),
    ('get_selected_values', lambda w: w.get_selected_values()),
    ('get_value', lambda w: w.get_value()),  # Handles NoneAwareCheckBox, NoneAwareIntEdit, etc.
    ('value', lambda w: None if (hasattr(w, 'specialValueText') and w.value() == w.minimum() and w.specialValueText()) else w.value()),
    ('get_path', lambda w: w.get_path()),  # EnhancedPathWidget support
    ('text', lambda w: w.text())
]

logger = logging.getLogger(__name__)

# Import our comprehensive shared infrastructure
from openhcs.ui.shared.parameter_form_service import ParameterFormService, ParameterInfo
from openhcs.ui.shared.parameter_form_config_factory import pyqt_config
from openhcs.ui.shared.parameter_form_constants import CONSTANTS

from openhcs.ui.shared.widget_creation_registry import create_pyqt6_registry
from openhcs.ui.shared.ui_utils import format_param_name, format_field_id, format_reset_button_id
from .widget_strategies import PyQt6WidgetEnhancer

# Import PyQt-specific components
from .clickable_help_components import GroupBoxWithHelp, LabelWithHelp
from openhcs.pyqt_gui.shared.color_scheme import PyQt6ColorScheme
from .layout_constants import CURRENT_LAYOUT

# Import OpenHCS core components
from openhcs.core.lazy_placeholder_simplified import LazyDefaultPlaceholderService
# Old field path detection removed - using simple field name matching
from openhcs.ui.shared.parameter_type_utils import ParameterTypeUtils





class NoneAwareLineEdit(QLineEdit):
    """QLineEdit that properly handles None values for lazy dataclass contexts."""

    def get_value(self):
        """Get value, returning None for empty text instead of empty string."""
        text = self.text().strip()
        return None if text == "" else text

    def set_value(self, value):
        """Set value, handling None properly."""
        self.setText("" if value is None else str(value))


class NoneAwareIntEdit(QLineEdit):
    """QLineEdit that only allows digits and properly handles None values for integer fields."""

    def __init__(self, parent=None):
        super().__init__(parent)
        # Set up input validation to only allow digits
        from PyQt6.QtGui import QIntValidator
        self.setValidator(QIntValidator())

    def get_value(self):
        """Get value, returning None for empty text or converting to int."""
        text = self.text().strip()
        if text == "":
            return None
        try:
            return int(text)
        except ValueError:
            return None

    def set_value(self, value):
        """Set value, handling None properly."""
        if value is None:
            self.setText("")
        else:
            self.setText(str(value))


class ParameterFormManager(QWidget):
    """
    PyQt6 parameter form manager with simplified implementation using generic object introspection.

    This implementation leverages the new context management system and supports any object type:
    - Dataclasses (via dataclasses.fields())
    - ABC constructors (via inspect.signature())
    - Step objects (via attribute scanning)
    - Any object with parameters

    Key improvements:
    - Generic object introspection replaces manual parameter specification
    - Context-driven resolution using config_context() system
    - Automatic parameter extraction from object instances
    - Unified interface for all object types
    - Dramatically simplified constructor (4 parameters vs 12+)
    """

    parameter_changed = pyqtSignal(str, object)  # param_name, value

    # Class constants for UI preferences (moved from constructor parameters)
    DEFAULT_USE_SCROLL_AREA = False
    DEFAULT_PLACEHOLDER_PREFIX = "Default"
    DEFAULT_COLOR_SCHEME = None

    def __init__(self, object_instance: Any, field_id: str, parent=None, context_obj=None, exclude_params: Optional[list] = None, initial_values: Optional[Dict[str, Any]] = None):
        """
        Initialize PyQt parameter form manager with generic object introspection.

        Args:
            object_instance: Any object to build form for (dataclass, ABC constructor, step, etc.)
            field_id: Unique identifier for the form
            parent: Optional parent widget
            context_obj: Context object for placeholder resolution (orchestrator, pipeline_config, etc.)
            exclude_params: Optional list of parameter names to exclude from the form
            initial_values: Optional dict of parameter values to use instead of extracted defaults
        """
        with timer(f"ParameterFormManager.__init__ ({field_id})", threshold_ms=5.0):
            QWidget.__init__(self, parent)

            # Store core configuration
            self.object_instance = object_instance
            self.field_id = field_id
            self.context_obj = context_obj
            self.exclude_params = exclude_params or []

            # Initialize service layer first (needed for parameter extraction)
            with timer("  Service initialization", threshold_ms=1.0):
                self.service = ParameterFormService()

            # Auto-extract parameters and types using generic introspection
            with timer("  Extract parameters from object", threshold_ms=2.0):
                self.parameters, self.parameter_types, self.dataclass_type = self._extract_parameters_from_object(object_instance, self.exclude_params)

                # CRITICAL FIX: Override with initial_values if provided (for function kwargs)
                if initial_values:
                    print(f"🔍 PARAM FORM: initial_values={initial_values}")
                    print(f"🔍 PARAM FORM: self.parameters BEFORE={self.parameters}")
                    for param_name, value in initial_values.items():
                        if param_name in self.parameters:
                            self.parameters[param_name] = value
                            print(f"🔍 PARAM FORM: Set {param_name}={value}")
                    print(f"🔍 PARAM FORM: self.parameters AFTER={self.parameters}")

            # DELEGATE TO SERVICE LAYER: Analyze form structure using service
            # Use UnifiedParameterAnalyzer-derived descriptions as the single source of truth
            with timer("  Analyze form structure", threshold_ms=5.0):
                parameter_info = getattr(self, '_parameter_descriptions', {})
                self.form_structure = self.service.analyze_parameters(
                    self.parameters, self.parameter_types, field_id, parameter_info, self.dataclass_type
                )

            # Auto-detect configuration settings
            with timer("  Auto-detect config settings", threshold_ms=1.0):
                self.global_config_type = self._auto_detect_global_config_type()
                self.placeholder_prefix = self.DEFAULT_PLACEHOLDER_PREFIX

            # Create configuration object with auto-detected settings
            with timer("  Create config object", threshold_ms=1.0):
                color_scheme = self.DEFAULT_COLOR_SCHEME or PyQt6ColorScheme()
                config = pyqt_config(
                    field_id=field_id,
                    color_scheme=color_scheme,
                    function_target=object_instance,  # Use object_instance as function_target
                    use_scroll_area=self.DEFAULT_USE_SCROLL_AREA
                )
                # IMPORTANT: Keep parameter_info consistent with the analyzer output to avoid losing descriptions
                config.parameter_info = parameter_info
                config.dataclass_type = self.dataclass_type
                config.global_config_type = self.global_config_type
                config.placeholder_prefix = self.placeholder_prefix

                # Auto-determine editing mode based on object type analysis
                config.is_lazy_dataclass = self._is_lazy_dataclass()
                config.is_global_config_editing = not config.is_lazy_dataclass

            # Initialize core attributes
            with timer("  Initialize core attributes", threshold_ms=1.0):
                self.config = config
                self.param_defaults = self._extract_parameter_defaults()
                import logging
                logger = logging.getLogger(__name__)
                logger.info(f"🔍 PARAM FORM MANAGER __init__: param_defaults = {self.param_defaults}")

            # Initialize tracking attributes
            self.widgets = {}
            self.reset_buttons = {}  # Track reset buttons for API compatibility
            self.nested_managers = {}
            self.reset_fields = set()  # Track fields that have been explicitly reset to show inheritance

            # Track which fields have been explicitly set by users
            self._user_set_fields: set = set()

            # Track if initial form load is complete (disable live updates during initial load)
            self._initial_load_complete = False

            # SHARED RESET STATE: Track reset fields across all nested managers within this form
            if hasattr(parent, 'shared_reset_fields'):
                # Nested manager: use parent's shared reset state
                self.shared_reset_fields = parent.shared_reset_fields
            else:
                # Root manager: create new shared reset state
                self.shared_reset_fields = set()

            # Store backward compatibility attributes
            self.parameter_info = config.parameter_info
            self.use_scroll_area = config.use_scroll_area
            self.function_target = config.function_target
            self.color_scheme = config.color_scheme

            # Form structure already analyzed above using UnifiedParameterAnalyzer descriptions

            # Get widget creator from registry
            self._widget_creator = create_pyqt6_registry()

            # Context system handles updates automatically
            self._context_event_coordinator = None

            # Set up UI
            with timer("  Setup UI (widget creation)", threshold_ms=10.0):
                self.setup_ui()

            # Connect parameter changes to live placeholder updates
            # When any field changes, refresh all placeholders using current form state
            # CRITICAL: Don't refresh during reset operations - reset handles placeholders itself
            self.parameter_changed.connect(lambda param_name, value: self._refresh_all_placeholders() if not getattr(self, '_in_reset', False) else None)

            # CRITICAL: Detect user-set fields for lazy dataclasses
            # Check which parameters were explicitly set (raw non-None values)
            with timer("  Detect user-set fields", threshold_ms=1.0):
                from dataclasses import is_dataclass
                if is_dataclass(object_instance):
                    for field_name, raw_value in self.parameters.items():
                        # SIMPLE RULE: Raw non-None = user-set, Raw None = inherited
                        if raw_value is not None:
                            self._user_set_fields.add(field_name)

            # CRITICAL FIX: Refresh placeholders AFTER user-set detection to show correct concrete/placeholder state
            with timer("  Initial placeholder refresh", threshold_ms=10.0):
                self._refresh_all_placeholders()

            # CRITICAL FIX: Ensure nested managers also get their placeholders refreshed after full hierarchy is built
            # This fixes the issue where nested dataclass placeholders don't load properly on initial form creation
            with timer("  Nested placeholder refresh", threshold_ms=5.0):
                self._apply_to_nested_managers(lambda name, manager: manager._refresh_all_placeholders())

            # Mark initial load as complete - enable live placeholder updates from now on
            self._initial_load_complete = True
            self._apply_to_nested_managers(lambda name, manager: setattr(manager, '_initial_load_complete', True))

            # CRITICAL: For root GlobalPipelineConfig, refresh placeholders AGAIN after initial load
            # This enables sibling inheritance using the loaded form values as overlay
            # The first refresh (line 233) uses static defaults only
            # This second refresh uses static defaults + loaded form values for sibling inheritance
            is_root_global_config = (self.config.is_global_config_editing and
                                     self.global_config_type is not None and
                                     self.context_obj is None)
            if is_root_global_config:
                with timer("  Root global config sibling inheritance refresh", threshold_ms=10.0):
                    self._refresh_all_placeholders()
                    self._apply_to_nested_managers(lambda name, manager: manager._refresh_all_placeholders())

    # ==================== GENERIC OBJECT INTROSPECTION METHODS ====================

    def _extract_parameters_from_object(self, obj: Any, exclude_params: Optional[list] = None) -> Tuple[Dict[str, Any], Dict[str, Type], Type]:
        """
        Extract parameters and types from any object using unified analysis.

        Uses the existing UnifiedParameterAnalyzer for consistent handling of all object types.

        Args:
            obj: Object to extract parameters from
            exclude_params: Optional list of parameter names to exclude
        """
        from openhcs.ui.shared.unified_parameter_analyzer import UnifiedParameterAnalyzer

        # Use unified analyzer for all object types with exclusions
        param_info_dict = UnifiedParameterAnalyzer.analyze(obj, exclude_params=exclude_params)

        parameters = {}
        parameter_types = {}

        # CRITICAL FIX: Store parameter descriptions for docstring display
        self._parameter_descriptions = {}

        for name, param_info in param_info_dict.items():
            # Use the values already extracted by UnifiedParameterAnalyzer
            # This preserves lazy config behavior (None values for unset fields)
            parameters[name] = param_info.default_value
            parameter_types[name] = param_info.param_type

            # LOG PARAMETER TYPES
            # CRITICAL FIX: Preserve parameter descriptions for help display
            if param_info.description:
                self._parameter_descriptions[name] = param_info.description

        return parameters, parameter_types, type(obj)

    # ==================== WIDGET CREATION METHODS ====================

    def _auto_detect_global_config_type(self) -> Optional[Type]:
        """Auto-detect global config type from context."""
        from openhcs.config_framework import get_base_config_type
        return getattr(self.context_obj, 'global_config_type', get_base_config_type())


    def _extract_parameter_defaults(self) -> Dict[str, Any]:
        """
        Extract parameter defaults from the object.

        For reset functionality: returns the SIGNATURE defaults, not current instance values.
        - For functions: signature defaults
        - For dataclasses: field defaults from class definition
        - For any object: constructor parameter defaults from class definition
        """
        from openhcs.ui.shared.unified_parameter_analyzer import UnifiedParameterAnalyzer
        import dataclasses

        # CRITICAL FIX: For reset functionality, we need SIGNATURE defaults, not instance values
        # Analyze the CLASS/TYPE, not the instance, to get signature defaults
        if callable(self.object_instance) and not dataclasses.is_dataclass(self.object_instance):
            # For functions/callables, analyze directly (not their type)
            analysis_target = self.object_instance
        elif dataclasses.is_dataclass(self.object_instance):
            # For dataclass instances, analyze the type to get field defaults
            analysis_target = type(self.object_instance)
        elif hasattr(self.object_instance, '__class__'):
            # For regular object instances (like steps), analyze the class to get constructor defaults
            analysis_target = type(self.object_instance)
        else:
            # For types/classes, analyze directly
            analysis_target = self.object_instance

        # Use unified analyzer to get signature defaults with same exclusions
        param_info_dict = UnifiedParameterAnalyzer.analyze(analysis_target, exclude_params=self.exclude_params)

        return {name: info.default_value for name, info in param_info_dict.items()}

    def _is_lazy_dataclass(self) -> bool:
        """Check if the object represents a lazy dataclass."""
        if hasattr(self.object_instance, '_resolve_field_value'):
            return True
        if self.dataclass_type:
            from openhcs.core.lazy_placeholder_simplified import LazyDefaultPlaceholderService
            return LazyDefaultPlaceholderService.has_lazy_resolution(self.dataclass_type)
        return False

    def create_widget(self, param_name: str, param_type: Type, current_value: Any,
                     widget_id: str, parameter_info: Any = None) -> Any:
        """Create widget using the registry creator function."""
        widget = self._widget_creator(param_name, param_type, current_value, widget_id, parameter_info)

        if widget is None:
            from PyQt6.QtWidgets import QLabel
            widget = QLabel(f"ERROR: Widget creation failed for {param_name}")

        return widget




    @classmethod
    def from_dataclass_instance(cls, dataclass_instance: Any, field_id: str,
                              placeholder_prefix: str = "Default",
                              parent=None, use_scroll_area: bool = True,
                              function_target=None, color_scheme=None,
                              force_show_all_fields: bool = False,
                              global_config_type: Optional[Type] = None,
                              context_event_coordinator=None, context_obj=None):
        """
        SIMPLIFIED: Create ParameterFormManager using new generic constructor.

        This method now simply delegates to the simplified constructor that handles
        all object types automatically through generic introspection.

        Args:
            dataclass_instance: The dataclass instance to edit
            field_id: Unique identifier for the form
            context_obj: Context object for placeholder resolution
            **kwargs: Legacy parameters (ignored - handled automatically)

        Returns:
            ParameterFormManager configured for any object type
        """
        # Validate input
        from dataclasses import is_dataclass
        if not is_dataclass(dataclass_instance):
            raise ValueError(f"{type(dataclass_instance)} is not a dataclass")

        # Use simplified constructor with automatic parameter extraction
        # CRITICAL: Do NOT default context_obj to dataclass_instance
        # This creates circular context bug where form uses itself as parent
        # Caller must explicitly pass context_obj if needed (e.g., Step Editor passes pipeline_config)
        return cls(
            object_instance=dataclass_instance,
            field_id=field_id,
            parent=parent,
            context_obj=context_obj  # No default - None means inherit from thread-local global only
        )

    @classmethod
    def from_object(cls, object_instance: Any, field_id: str, parent=None, context_obj=None):
        """
        NEW: Create ParameterFormManager for any object type using generic introspection.

        This is the new primary factory method that works with:
        - Dataclass instances and types
        - ABC constructors and functions
        - Step objects with config attributes
        - Any object with parameters

        Args:
            object_instance: Any object to build form for
            field_id: Unique identifier for the form
            parent: Optional parent widget
            context_obj: Context object for placeholder resolution

        Returns:
            ParameterFormManager configured for the object type
        """
        return cls(
            object_instance=object_instance,
            field_id=field_id,
            parent=parent,
            context_obj=context_obj
        )



    def setup_ui(self):
        """Set up the UI layout."""
        layout = QVBoxLayout(self)
        # Apply configurable layout settings
        layout.setSpacing(CURRENT_LAYOUT.main_layout_spacing)
        layout.setContentsMargins(*CURRENT_LAYOUT.main_layout_margins)

        # Apply centralized widget styling for uniform appearance (same as config_window.py)
        from openhcs.pyqt_gui.shared.style_generator import StyleSheetGenerator
        style_gen = StyleSheetGenerator(self.color_scheme)
        self.setStyleSheet(style_gen.generate_config_window_style())

        # Build form content
        form_widget = self.build_form()

        # Add scroll area if requested
        if self.config.use_scroll_area:
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            scroll_area.setWidget(form_widget)
            layout.addWidget(scroll_area)
        else:
            layout.addWidget(form_widget)

    def build_form(self) -> QWidget:
        """Build form UI by delegating to service layer analysis."""
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(CURRENT_LAYOUT.content_layout_spacing)
        content_layout.setContentsMargins(*CURRENT_LAYOUT.content_layout_margins)

        # DELEGATE TO SERVICE LAYER: Use analyzed form structure
        for param_info in self.form_structure.parameters:
            if param_info.is_optional and param_info.is_nested:
                # Optional[Dataclass]: show checkbox
                widget = self._create_optional_dataclass_widget(param_info)
            elif param_info.is_nested:
                # Direct dataclass (non-optional): nested group without checkbox
                widget = self._create_nested_dataclass_widget(param_info)
            else:
                # All regular types (including Optional[regular]) use regular widgets with None-aware behavior
                widget = self._create_regular_parameter_widget(param_info)
            content_layout.addWidget(widget)

        return content_widget

    def _create_regular_parameter_widget(self, param_info) -> QWidget:
        """Create widget for regular parameter - DELEGATE TO SERVICE LAYER."""
        display_info = self.service.get_parameter_display_info(param_info.name, param_info.type, param_info.description)
        field_ids = self.service.generate_field_ids_direct(self.config.field_id, param_info.name)

        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setSpacing(CURRENT_LAYOUT.parameter_row_spacing)
        layout.setContentsMargins(*CURRENT_LAYOUT.parameter_row_margins)

        # Label
        label = LabelWithHelp(
            text=display_info['field_label'], param_name=param_info.name,
            param_description=display_info['description'], param_type=param_info.type,
            color_scheme=self.config.color_scheme or PyQt6ColorScheme()
        )
        layout.addWidget(label)

        # Widget
        current_value = self.parameters.get(param_info.name)
        print(f"🔍 CREATE WIDGET: {param_info.name} current_value={current_value} from self.parameters")
        widget = self.create_widget(param_info.name, param_info.type, current_value, field_ids['widget_id'])
        widget.setObjectName(field_ids['widget_id'])
        layout.addWidget(widget, 1)

        # Reset button
        reset_button = QPushButton(CONSTANTS.RESET_BUTTON_TEXT)
        reset_button.setObjectName(field_ids['reset_button_id'])
        reset_button.setMaximumWidth(CURRENT_LAYOUT.reset_button_width)
        reset_button.clicked.connect(lambda: self.reset_parameter(param_info.name))
        layout.addWidget(reset_button)

        # Store widgets and connect signals
        self.widgets[param_info.name] = widget
        PyQt6WidgetEnhancer.connect_change_signal(widget, param_info.name, self._emit_parameter_change)

        # CRITICAL FIX: Apply placeholder behavior after widget creation
        current_value = self.parameters.get(param_info.name)
        self._apply_context_behavior(widget, current_value, param_info.name)

        return container

    def _create_optional_regular_widget(self, param_info) -> QWidget:
        """Create widget for Optional[regular_type] - checkbox + regular widget."""
        display_info = self.service.get_parameter_display_info(param_info.name, param_info.type, param_info.description)
        field_ids = self.service.generate_field_ids_direct(self.config.field_id, param_info.name)

        container = QWidget()
        layout = QVBoxLayout(container)

        # Checkbox (using NoneAwareCheckBox for consistency)
        from openhcs.pyqt_gui.widgets.shared.no_scroll_spinbox import NoneAwareCheckBox
        checkbox = NoneAwareCheckBox()
        checkbox.setText(display_info['checkbox_label'])
        checkbox.setObjectName(field_ids['optional_checkbox_id'])
        current_value = self.parameters.get(param_info.name)
        checkbox.setChecked(current_value is not None)
        layout.addWidget(checkbox)

        # Get inner type for the actual widget
        from openhcs.ui.shared.parameter_type_utils import ParameterTypeUtils
        inner_type = ParameterTypeUtils.get_optional_inner_type(param_info.type)

        # Create the actual widget for the inner type
        inner_widget = self._create_regular_parameter_widget_for_type(param_info.name, inner_type, current_value)
        inner_widget.setEnabled(current_value is not None)  # Disable if None
        layout.addWidget(inner_widget)

        # Connect checkbox to enable/disable the inner widget
        def on_checkbox_changed(checked):
            inner_widget.setEnabled(checked)
            if checked:
                # Set to default value for the inner type
                if inner_type == str:
                    default_value = ""
                elif inner_type == int:
                    default_value = 0
                elif inner_type == float:
                    default_value = 0.0
                elif inner_type == bool:
                    default_value = False
                else:
                    default_value = None
                self.update_parameter(param_info.name, default_value)
            else:
                self.update_parameter(param_info.name, None)

        checkbox.toggled.connect(on_checkbox_changed)
        return container

    def _create_regular_parameter_widget_for_type(self, param_name: str, param_type: Type, current_value: Any) -> QWidget:
        """Create a regular parameter widget for a specific type."""
        field_ids = self.service.generate_field_ids_direct(self.config.field_id, param_name)

        # Use the existing create_widget method
        widget = self.create_widget(param_name, param_type, current_value, field_ids['widget_id'])
        if widget:
            return widget

        # Fallback to basic text input
        from PyQt6.QtWidgets import QLineEdit
        fallback_widget = QLineEdit()
        fallback_widget.setText(str(current_value or ""))
        fallback_widget.setObjectName(field_ids['widget_id'])
        return fallback_widget

    def _create_nested_dataclass_widget(self, param_info) -> QWidget:
        """Create widget for nested dataclass - DELEGATE TO SERVICE LAYER."""
        display_info = self.service.get_parameter_display_info(param_info.name, param_info.type, param_info.description)

        # Always use the inner dataclass type for Optional[T] when wiring help/paths
        from openhcs.ui.shared.parameter_type_utils import ParameterTypeUtils
        unwrapped_type = (
            ParameterTypeUtils.get_optional_inner_type(param_info.type)
            if ParameterTypeUtils.is_optional_dataclass(param_info.type)
            else param_info.type
        )

        group_box = GroupBoxWithHelp(
            title=display_info['field_label'], help_target=unwrapped_type,
            color_scheme=self.config.color_scheme or PyQt6ColorScheme()
        )
        current_value = self.parameters.get(param_info.name)
        nested_manager = self._create_nested_form_inline(param_info.name, unwrapped_type, current_value)

        nested_form = nested_manager.build_form()

        # Use GroupBoxWithHelp's addWidget method instead of creating our own layout
        group_box.addWidget(nested_form)

        self.nested_managers[param_info.name] = nested_manager
        return group_box

    def _create_optional_dataclass_widget(self, param_info) -> QWidget:
        """Create widget for optional dataclass - checkbox integrated into GroupBox title."""
        display_info = self.service.get_parameter_display_info(param_info.name, param_info.type, param_info.description)
        field_ids = self.service.generate_field_ids_direct(self.config.field_id, param_info.name)

        # Get the unwrapped type for the GroupBox
        from openhcs.ui.shared.parameter_type_utils import ParameterTypeUtils
        unwrapped_type = ParameterTypeUtils.get_optional_inner_type(param_info.type)

        # Create GroupBox with custom title widget that includes checkbox
        from PyQt6.QtGui import QFont
        group_box = QGroupBox()

        # Create custom title widget with checkbox + title + help button (all inline)
        title_widget = QWidget()
        title_layout = QHBoxLayout(title_widget)
        title_layout.setSpacing(5)
        title_layout.setContentsMargins(10, 5, 10, 5)

        # Checkbox (compact, no text)
        from openhcs.pyqt_gui.widgets.shared.no_scroll_spinbox import NoneAwareCheckBox
        checkbox = NoneAwareCheckBox()
        checkbox.setObjectName(field_ids['optional_checkbox_id'])
        current_value = self.parameters.get(param_info.name)
        checkbox.setChecked(current_value is not None)
        checkbox.setMaximumWidth(20)
        title_layout.addWidget(checkbox)

        # Title label (clickable to toggle checkbox, matches GroupBoxWithHelp styling)
        title_label = QLabel(display_info['checkbox_label'])
        title_font = QFont()
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.mousePressEvent = lambda e: checkbox.toggle()
        title_label.setCursor(Qt.CursorShape.PointingHandCursor)
        title_layout.addWidget(title_label)

        # Help button (matches GroupBoxWithHelp)
        from openhcs.pyqt_gui.widgets.shared.clickable_help_components import HelpButton
        help_btn = HelpButton(help_target=unwrapped_type, text="?", color_scheme=self.color_scheme)
        help_btn.setMaximumWidth(25)
        help_btn.setMaximumHeight(20)
        title_layout.addWidget(help_btn)

        title_layout.addStretch()

        # Set the custom title widget as the GroupBox title
        group_box.setLayout(QVBoxLayout())
        group_box.layout().setSpacing(0)
        group_box.layout().setContentsMargins(0, 0, 0, 0)
        group_box.layout().addWidget(title_widget)

        # Create nested form
        nested_manager = self._create_nested_form_inline(param_info.name, unwrapped_type, current_value)
        nested_form = nested_manager.build_form()
        nested_form.setEnabled(current_value is not None)
        group_box.layout().addWidget(nested_form)

        self.nested_managers[param_info.name] = nested_manager

        # Connect checkbox to enable/disable with visual feedback
        def on_checkbox_changed(checked):
            nested_form.setEnabled(checked)
            # Apply visual feedback to all input widgets
            if checked:
                # Restore normal color (no explicit style needed - font is already bold)
                title_label.setStyleSheet("")
                help_btn.setEnabled(True)
                # Remove dimming from all widgets
                for widget in nested_form.findChildren(QWidget):
                    widget.setGraphicsEffect(None)
                # Create default instance
                default_instance = unwrapped_type()
                self.update_parameter(param_info.name, default_instance)
            else:
                # Dim title text but keep help button enabled
                title_label.setStyleSheet(f"color: {self.color_scheme.to_hex(self.color_scheme.text_disabled)};")
                help_btn.setEnabled(True)  # Keep help button clickable even when disabled
                # Dim all input widgets
                from PyQt6.QtWidgets import QGraphicsOpacityEffect
                for widget in nested_form.findChildren((QLineEdit, QComboBox, QPushButton)):
                    effect = QGraphicsOpacityEffect()
                    effect.setOpacity(0.4)
                    widget.setGraphicsEffect(effect)
                self.update_parameter(param_info.name, None)

        checkbox.toggled.connect(on_checkbox_changed)
        on_checkbox_changed(checkbox.isChecked())

        self.widgets[param_info.name] = group_box
        return group_box









    def _create_nested_form_inline(self, param_name: str, param_type: Type, current_value: Any) -> Any:
        """Create nested form - simplified to let constructor handle parameter extraction"""
        # Get actual field path from FieldPathDetector (no artificial "nested_" prefix)
        # For function parameters (no parent dataclass), use parameter name directly
        if self.dataclass_type is None:
            field_path = param_name
        else:
            field_path = self.service.get_field_path_with_fail_loud(self.dataclass_type, param_type)

        # Use current_value if available, otherwise create a default instance of the dataclass type
        # The constructor will handle parameter extraction automatically
        if current_value is not None:
            # If current_value is a dict (saved config), convert it back to dataclass instance
            import dataclasses
            # Unwrap Optional type to get actual dataclass type
            from openhcs.ui.shared.parameter_type_utils import ParameterTypeUtils
            actual_type = ParameterTypeUtils.get_optional_inner_type(param_type) if ParameterTypeUtils.is_optional(param_type) else param_type

            if isinstance(current_value, dict) and dataclasses.is_dataclass(actual_type):
                # Convert dict back to dataclass instance
                object_instance = actual_type(**current_value)
            else:
                object_instance = current_value
        else:
            # Create a default instance of the dataclass type for parameter extraction
            import dataclasses
            # Unwrap Optional type to get actual dataclass type
            from openhcs.ui.shared.parameter_type_utils import ParameterTypeUtils
            actual_type = ParameterTypeUtils.get_optional_inner_type(param_type) if ParameterTypeUtils.is_optional(param_type) else param_type

            if dataclasses.is_dataclass(actual_type):
                object_instance = actual_type()
            else:
                object_instance = actual_type

        # DELEGATE TO NEW CONSTRUCTOR: Use simplified constructor
        nested_manager = ParameterFormManager(
            object_instance=object_instance,
            field_id=field_path,
            parent=self,
            context_obj=self.context_obj
        )
        # Inherit lazy/global editing context from parent so resets behave correctly in nested forms
        try:
            nested_manager.config.is_lazy_dataclass = self.config.is_lazy_dataclass
            nested_manager.config.is_global_config_editing = not self.config.is_lazy_dataclass
        except Exception:
            pass

        # Store parent manager reference for placeholder resolution
        nested_manager._parent_manager = self

        # Connect nested manager's parameter_changed signal to parent's refresh handler
        # This ensures changes in nested forms trigger placeholder updates in parent and siblings
        nested_manager.parameter_changed.connect(self._on_nested_parameter_changed)

        # Store nested manager
        self.nested_managers[param_name] = nested_manager

        return nested_manager



    def _convert_widget_value(self, value: Any, param_name: str) -> Any:
        """
        Convert widget value to proper type.

        Applies both PyQt-specific conversions (Path, tuple/list parsing) and
        service layer conversions (enums, basic types, Union handling).
        """
        from openhcs.pyqt_gui.widgets.shared.widget_strategies import convert_widget_value_to_type

        param_type = self.parameter_types.get(param_name, type(value))

        # PyQt-specific type conversions first
        converted_value = convert_widget_value_to_type(value, param_type)

        # Then apply service layer conversion (enums, basic types, Union handling, etc.)
        converted_value = self.service.convert_value_to_type(converted_value, param_type, param_name, self.dataclass_type)

        return converted_value

    def _emit_parameter_change(self, param_name: str, value: Any) -> None:
        """Handle parameter change from widget and update parameter data model."""
        # Convert value using unified conversion method
        converted_value = self._convert_widget_value(value, param_name)

        # Update parameter in data model
        self.parameters[param_name] = converted_value

        # CRITICAL FIX: Track that user explicitly set this field
        # This prevents placeholder updates from destroying user values
        self._user_set_fields.add(param_name)

        # Emit signal only once - this triggers sibling placeholder updates
        self.parameter_changed.emit(param_name, converted_value)



    def update_widget_value(self, widget: QWidget, value: Any, param_name: str = None, skip_context_behavior: bool = False, exclude_field: str = None) -> None:
        """Mathematical simplification: Unified widget update using shared dispatch."""
        self._execute_with_signal_blocking(widget, lambda: self._dispatch_widget_update(widget, value))

        # Only apply context behavior if not explicitly skipped (e.g., during reset operations)
        if not skip_context_behavior:
            self._apply_context_behavior(widget, value, param_name, exclude_field)

    def _dispatch_widget_update(self, widget: QWidget, value: Any) -> None:
        """Algebraic simplification: Single dispatch logic for all widget updates."""
        for matcher, updater in WIDGET_UPDATE_DISPATCH:
            if isinstance(widget, matcher) if isinstance(matcher, type) else hasattr(widget, matcher):
                if isinstance(updater, str):
                    getattr(self, f'_{updater}')(widget, value)
                else:
                    updater(widget, value)
                return

    def _clear_widget_to_default_state(self, widget: QWidget) -> None:
        """Clear widget to its default/empty state for reset operations."""
        from PyQt6.QtWidgets import QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox, QCheckBox, QTextEdit

        if isinstance(widget, QLineEdit):
            widget.clear()
        elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
            widget.setValue(widget.minimum())
        elif isinstance(widget, QComboBox):
            widget.setCurrentIndex(-1)  # No selection
        elif isinstance(widget, QCheckBox):
            widget.setChecked(False)
        elif isinstance(widget, QTextEdit):
            widget.clear()
        else:
            # For custom widgets, try to call clear() if available
            if hasattr(widget, 'clear'):
                widget.clear()

    def _update_combo_box(self, widget: QComboBox, value: Any) -> None:
        """Update combo box with value matching."""
        widget.setCurrentIndex(-1 if value is None else
                             next((i for i in range(widget.count()) if widget.itemData(i) == value), -1))

    def _update_checkbox_group(self, widget: QWidget, value: Any) -> None:
        """Update checkbox group using functional operations."""
        if hasattr(widget, '_checkboxes') and isinstance(value, list):
            # Functional: reset all, then set selected
            [cb.setChecked(False) for cb in widget._checkboxes.values()]
            [widget._checkboxes[v].setChecked(True) for v in value if v in widget._checkboxes]

    def _execute_with_signal_blocking(self, widget: QWidget, operation: callable) -> None:
        """Execute operation with signal blocking - stateless utility."""
        widget.blockSignals(True)
        operation()
        widget.blockSignals(False)

    def _apply_context_behavior(self, widget: QWidget, value: Any, param_name: str, exclude_field: str = None) -> None:
        """CONSOLIDATED: Apply placeholder behavior using single resolution path."""
        if not param_name or not self.dataclass_type:
            return

        if value is None:
            # Allow placeholder application for nested forms even if they're not detected as lazy dataclasses
            # The placeholder service will determine if placeholders are available

            # Build overlay from current form state
            overlay = self.get_current_values()

            # Build context stack: parent context + overlay
            with self._build_context_stack(overlay):
                placeholder_text = self.service.get_placeholder_text(param_name, self.dataclass_type)
                if placeholder_text:
                    PyQt6WidgetEnhancer.apply_placeholder_text(widget, placeholder_text)
        elif value is not None:
            PyQt6WidgetEnhancer._clear_placeholder_state(widget)


    def get_widget_value(self, widget: QWidget) -> Any:
        """Mathematical simplification: Unified widget value extraction using shared dispatch."""
        for matcher, extractor in WIDGET_GET_DISPATCH:
            if isinstance(widget, matcher) if isinstance(matcher, type) else hasattr(widget, matcher):
                return extractor(widget)
        return None

    # Framework-specific methods for backward compatibility

    def reset_all_parameters(self) -> None:
        """Reset all parameters - let reset_parameter handle everything."""
        try:
            # CRITICAL FIX: Create a copy of keys to avoid "dictionary changed during iteration" error
            # reset_parameter can modify self.parameters by removing keys, so we need a stable list
            param_names = list(self.parameters.keys())
            for param_name in param_names:
                self.reset_parameter(param_name)

            # Also refresh placeholders in nested managers after recursive resets
            self._apply_to_nested_managers(lambda name, manager: manager._refresh_all_placeholders())

            # Handle nested managers once at the end
            if self.dataclass_type and self.nested_managers:
                current_config = getattr(self, '_current_config_instance', None)
                if current_config:
                    self.service.reset_nested_managers(self.nested_managers, self.dataclass_type, current_config)
        finally:
            # Context system handles placeholder updates automatically
            self._refresh_all_placeholders()



    def update_parameter(self, param_name: str, value: Any) -> None:
        """Update parameter value using shared service layer."""

        if param_name in self.parameters:
            # Convert value using service layer
            converted_value = self.service.convert_value_to_type(value, self.parameter_types.get(param_name, type(value)), param_name, self.dataclass_type)

            # Update parameter in data model
            self.parameters[param_name] = converted_value

            # CRITICAL FIX: Track that user explicitly set this field
            # This prevents placeholder updates from destroying user values
            self._user_set_fields.add(param_name)

            # Update corresponding widget if it exists
            if param_name in self.widgets:
                self.update_widget_value(self.widgets[param_name], converted_value)

            # Emit signal for PyQt6 compatibility
            self.parameter_changed.emit(param_name, converted_value)

    def _is_function_parameter(self, param_name: str) -> bool:
        """
        Detect if parameter is a function parameter vs dataclass field.

        Function parameters should not be reset against dataclass types.
        This prevents the critical bug where step editor tries to reset
        function parameters like 'group_by' against the global config type.
        """
        if not self.function_target or not self.dataclass_type:
            return False

        # Check if parameter exists in dataclass fields
        import dataclasses
        if dataclasses.is_dataclass(self.dataclass_type):
            field_names = {field.name for field in dataclasses.fields(self.dataclass_type)}
            is_function_param = param_name not in field_names
            return is_function_param

        return False

    def reset_parameter(self, param_name: str) -> None:
        """Reset parameter to signature default."""
        if param_name not in self.parameters:
            return

        # Set flag to prevent _refresh_all_placeholders during reset
        self._in_reset = True
        try:
            return self._reset_parameter_impl(param_name)
        finally:
            self._in_reset = False

    def _reset_parameter_impl(self, param_name: str) -> None:
        """Internal reset implementation."""
        import logging
        logger = logging.getLogger(__name__)

        # Function parameters reset to static defaults from param_defaults
        if self._is_function_parameter(param_name):
            reset_value = self.param_defaults.get(param_name) if hasattr(self, 'param_defaults') else None
            logger.info(f"🔍 RESET_IMPL: Function parameter {param_name}, reset_value={reset_value}")
            self.parameters[param_name] = reset_value

            if param_name in self.widgets:
                widget = self.widgets[param_name]
                logger.info(f"🔍 RESET_IMPL: Updating widget for {param_name} to {reset_value}")
                self.update_widget_value(widget, reset_value, param_name, skip_context_behavior=True)
                # Verify widget was updated
                actual_value = self.get_widget_value(widget)
                logger.info(f"🔍 RESET_IMPL: Widget value after update: {actual_value}")

            self.parameter_changed.emit(param_name, reset_value)
            return

        # Special handling for dataclass fields
        try:
            import dataclasses as _dc
            from openhcs.ui.shared.parameter_type_utils import ParameterTypeUtils
            param_type = self.parameter_types.get(param_name)

            # If this is an Optional[Dataclass], sync container UI and reset nested manager
            if param_type and ParameterTypeUtils.is_optional_dataclass(param_type):
                reset_value = self._get_reset_value(param_name)
                self.parameters[param_name] = reset_value

                if param_name in self.widgets:
                    container = self.widgets[param_name]
                    # Toggle the optional checkbox to match reset_value (None -> unchecked)
                    from PyQt6.QtWidgets import QCheckBox
                    ids = self.service.generate_field_ids_direct(self.config.field_id, param_name)
                    checkbox = container.findChild(QCheckBox, ids['optional_checkbox_id'])
                    if checkbox:
                        checkbox.blockSignals(True)
                        checkbox.setChecked(reset_value is not None)
                        checkbox.blockSignals(False)

                # Reset nested manager contents too
                nested_manager = self.nested_managers.get(param_name)
                if nested_manager and hasattr(nested_manager, 'reset_all_parameters'):
                    nested_manager.reset_all_parameters()

                # Enable/disable the nested group visually without relying on signals
                try:
                    from .clickable_help_components import GroupBoxWithHelp
                    group = container.findChild(GroupBoxWithHelp) if param_name in self.widgets else None
                    if group:
                        group.setEnabled(reset_value is not None)
                except Exception:
                    pass

                # Emit parameter change and return (handled)
                self.parameter_changed.emit(param_name, reset_value)
                return

            # If this is a direct dataclass field (non-optional), do NOT replace the instance.
            # Instead, keep the container value and recursively reset the nested manager.
            if param_type and _dc.is_dataclass(param_type):
                nested_manager = self.nested_managers.get(param_name)
                if nested_manager and hasattr(nested_manager, 'reset_all_parameters'):
                    nested_manager.reset_all_parameters()
                # Do not modify self.parameters[param_name] (keep current dataclass instance)
                # Refresh placeholder on the group container if it has a widget
                if param_name in self.widgets:
                    self._apply_context_behavior(self.widgets[param_name], None, param_name)
                # Emit parameter change with unchanged container value
                self.parameter_changed.emit(param_name, self.parameters.get(param_name))
                return
        except Exception:
            # Fall through to generic handling if type checks fail
            pass

        # Generic config field reset - use context-aware reset value
        reset_value = self._get_reset_value(param_name)
        logger.info(f"🔍 RESET_IMPL: Generic field {param_name}, reset_value={reset_value} (from _get_reset_value)")
        self.parameters[param_name] = reset_value

        # Track reset fields only for lazy behavior (when reset_value is None)
        if reset_value is None:
            self.reset_fields.add(param_name)
            # SHARED RESET STATE: Also add to shared reset state for coordination with nested managers
            field_path = f"{self.field_id}.{param_name}"
            self.shared_reset_fields.add(field_path)
        else:
            # For concrete values, remove from reset tracking
            self.reset_fields.discard(param_name)
            field_path = f"{self.field_id}.{param_name}"
            self.shared_reset_fields.discard(field_path)

        # Update widget with reset value
        if param_name in self.widgets:
            widget = self.widgets[param_name]
            logger.info(f"🔍 RESET_IMPL: Updating widget for {param_name} to {reset_value}")
            self.update_widget_value(widget, reset_value, param_name)
            # Verify widget was updated
            actual_value = self.get_widget_value(widget)
            logger.info(f"🔍 RESET_IMPL: Widget value after update: {actual_value}")

            # Apply placeholder only if reset value is None (lazy behavior)
            if reset_value is None:
                # Build overlay from current form state
                overlay = self.get_current_values()

                # Build context stack (handles static defaults for global config editing)
                with self._build_context_stack(overlay):
                    placeholder_text = self.service.get_placeholder_text(param_name, self.dataclass_type)
                    if placeholder_text:
                        from openhcs.pyqt_gui.widgets.shared.widget_strategies import PyQt6WidgetEnhancer
                        PyQt6WidgetEnhancer.apply_placeholder_text(widget, placeholder_text)

        # Emit parameter change to notify other components
        self.parameter_changed.emit(param_name, reset_value)

    def _get_reset_value(self, param_name: str) -> Any:
        """Get reset value based on editing context.

        For global config editing: Use static class defaults (not None)
        For lazy config editing: Use signature defaults (None for inheritance)
        For functions: Use signature defaults
        """
        # For global config editing, use static class defaults instead of None
        if self.config.is_global_config_editing and self.dataclass_type:
            # Get static default from class attribute
            try:
                static_default = object.__getattribute__(self.dataclass_type, param_name)
                return static_default
            except AttributeError:
                # Fallback to signature default if no class attribute
                pass

        # For everything else, use signature defaults
        return self.param_defaults.get(param_name)



    def get_current_values(self) -> Dict[str, Any]:
        """
        Get current parameter values preserving lazy dataclass structure.

        This fixes the lazy default materialization override saving issue by ensuring
        that lazy dataclasses maintain their structure when values are retrieved.
        """
        with timer(f"get_current_values ({self.field_id})", threshold_ms=2.0):
            # CRITICAL FIX: Read actual current values from widgets, not initial parameters
            current_values = {}

            # Read current values from widgets
            for param_name in self.parameters.keys():
                widget = self.widgets.get(param_name)
                if widget:
                    raw_value = self.get_widget_value(widget)
                    # Apply unified type conversion
                    current_values[param_name] = self._convert_widget_value(raw_value, param_name)
                else:
                    # Fallback to initial parameter value if no widget
                    current_values[param_name] = self.parameters.get(param_name)

            # Checkbox validation is handled in widget creation

            # Collect values from nested managers, respecting optional dataclass checkbox states
            self._apply_to_nested_managers(
                lambda name, manager: self._process_nested_values_if_checkbox_enabled(
                    name, manager, current_values
                )
            )

            # Lazy dataclasses are now handled by LazyDataclassEditor, so no structure preservation needed
            return current_values

    def get_user_modified_values(self) -> Dict[str, Any]:
        """
        Get only values that were explicitly set by the user (non-None raw values).

        For lazy dataclasses, this preserves lazy resolution for unmodified fields
        by only returning fields where the raw value is not None.

        For nested dataclasses, only include them if they have user-modified fields inside.
        """
        if not hasattr(self.config, '_resolve_field_value'):
            # For non-lazy dataclasses, return all current values
            return self.get_current_values()

        user_modified = {}
        current_values = self.get_current_values()

        # Only include fields where the raw value is not None
        for field_name, value in current_values.items():
            if value is not None:
                # CRITICAL: For nested dataclasses, extract raw values to prevent resolution pollution
                # We need to rebuild the nested dataclass with only raw non-None values
                from dataclasses import is_dataclass, fields as dataclass_fields
                if is_dataclass(value) and not isinstance(value, type):
                    # Extract raw field values from nested dataclass
                    nested_raw_values = {}
                    for field in dataclass_fields(value):
                        raw_value = object.__getattribute__(value, field.name)
                        if raw_value is not None:
                            nested_raw_values[field.name] = raw_value

                    # Only include if nested dataclass has user-modified fields
                    # Recreate the instance with only raw values
                    if nested_raw_values:
                        user_modified[field_name] = type(value)(**nested_raw_values)
                else:
                    # Non-dataclass field, include if not None
                    user_modified[field_name] = value

        return user_modified

    def _build_context_stack(self, overlay, skip_parent_overlay: bool = False):
        """Build nested config_context() calls for placeholder resolution.

        Context stack order for PipelineConfig (lazy):
        1. Thread-local global config (automatic base - loaded instance)
        2. Parent context(s) from self.context_obj (if provided)
        3. Parent overlay (if nested form)
        4. Overlay from current form values (always applied last)

        Context stack order for GlobalPipelineConfig (non-lazy):
        1. Thread-local global config (automatic base - loaded instance)
        2. Static defaults (masks thread-local with fresh GlobalPipelineConfig())
        3. Overlay from current form values (always applied last)

        Args:
            overlay: Current form values (from get_current_values()) - dict or dataclass instance
            skip_parent_overlay: If True, skip applying parent's user-modified values.
                                Used during reset to prevent parent from re-introducing old values.

        Returns:
            ExitStack with nested contexts
        """
        from contextlib import ExitStack
        from openhcs.config_framework.context_manager import config_context

        stack = ExitStack()

        # CRITICAL: For GlobalPipelineConfig editing (root form only), apply static defaults as base context
        # This masks the thread-local loaded instance with class defaults
        # Only do this for the ROOT GlobalPipelineConfig form, not nested configs or step editor
        is_root_global_config = (self.config.is_global_config_editing and
                                 self.global_config_type is not None and
                                 self.context_obj is None)  # No parent context = root form

        if is_root_global_config:
            static_defaults = self.global_config_type()
            stack.enter_context(config_context(static_defaults, mask_with_none=True))

        # Apply parent context(s) if provided
        if self.context_obj is not None:
            if isinstance(self.context_obj, list):
                # Multiple parent contexts (future: deeply nested editors)
                for ctx in self.context_obj:
                    stack.enter_context(config_context(ctx))
            else:
                # Single parent context (Step Editor: pipeline_config)
                stack.enter_context(config_context(self.context_obj))

        # CRITICAL: For nested forms, include parent's USER-MODIFIED values for sibling inheritance
        # This allows live placeholder updates when sibling fields change
        # ONLY enable this AFTER initial form load to avoid polluting placeholders with initial widget values
        # SKIP if skip_parent_overlay=True (used during reset to prevent re-introducing old values)
        parent_manager = getattr(self, '_parent_manager', None)
        if (not skip_parent_overlay and
            parent_manager and
            hasattr(parent_manager, 'get_user_modified_values') and
            hasattr(parent_manager, 'dataclass_type') and
            parent_manager._initial_load_complete):  # Check PARENT's initial load flag

            # Get only user-modified values from parent (not all values)
            # This prevents polluting context with stale/default values
            parent_user_values = parent_manager.get_user_modified_values()

            if parent_user_values and parent_manager.dataclass_type:
                # CRITICAL: Exclude the current nested config from parent overlay
                # This prevents the parent from re-introducing old values when resetting fields in nested form
                # Example: When resetting well_filter in StepMaterializationConfig, don't include
                # step_materialization_config from parent's user-modified values
                # CRITICAL FIX: Also exclude params from parent's exclude_params list (e.g., 'func' for FunctionStep)
                excluded_keys = {self.field_id}
                if hasattr(parent_manager, 'exclude_params') and parent_manager.exclude_params:
                    excluded_keys.update(parent_manager.exclude_params)

                filtered_parent_values = {k: v for k, v in parent_user_values.items() if k not in excluded_keys}

                if filtered_parent_values:
                    # Use lazy version of parent type to enable sibling inheritance
                    from openhcs.core.lazy_placeholder_simplified import LazyDefaultPlaceholderService
                    parent_type = parent_manager.dataclass_type
                    lazy_parent_type = LazyDefaultPlaceholderService._get_lazy_type_for_base(parent_type)
                    if lazy_parent_type:
                        parent_type = lazy_parent_type

                    # CRITICAL FIX: Add excluded params from parent's object_instance
                    # This allows instantiating parent_type even when some params are excluded from the form
                    parent_values_with_excluded = filtered_parent_values.copy()
                    if hasattr(parent_manager, 'exclude_params') and parent_manager.exclude_params:
                        for excluded_param in parent_manager.exclude_params:
                            if excluded_param not in parent_values_with_excluded and hasattr(parent_manager.object_instance, excluded_param):
                                parent_values_with_excluded[excluded_param] = getattr(parent_manager.object_instance, excluded_param)

                    # Create parent overlay with only user-modified values (excluding current nested config)
                    # For global config editing (root form only), use mask_with_none=True to preserve None overrides
                    parent_overlay_instance = parent_type(**parent_values_with_excluded)
                    if is_root_global_config:
                        stack.enter_context(config_context(parent_overlay_instance, mask_with_none=True))
                    else:
                        stack.enter_context(config_context(parent_overlay_instance))

        # Convert overlay dict to object instance for config_context()
        # config_context() expects an object with attributes, not a dict
        if isinstance(overlay, dict) and self.dataclass_type:
            # CRITICAL FIX: For excluded params (e.g., 'func' for FunctionStep), use values from object_instance
            # This allows us to instantiate the dataclass type while excluding certain params from the overlay
            overlay_with_excluded = overlay.copy()
            for excluded_param in self.exclude_params:
                if excluded_param not in overlay_with_excluded and hasattr(self.object_instance, excluded_param):
                    # Use the value from the original object instance for excluded params
                    overlay_with_excluded[excluded_param] = getattr(self.object_instance, excluded_param)

            # For functions and non-dataclass objects: use SimpleNamespace to hold parameters
            # For dataclasses: instantiate normally
            try:
                overlay_instance = self.dataclass_type(**overlay_with_excluded)
            except TypeError:
                # Function or other non-instantiable type: use SimpleNamespace
                from types import SimpleNamespace
                # For SimpleNamespace, we don't need excluded params
                filtered_overlay = {k: v for k, v in overlay.items() if k not in self.exclude_params}
                overlay_instance = SimpleNamespace(**filtered_overlay)
        else:
            overlay_instance = overlay

        # Always apply overlay with current form values (the object being edited)
        # config_context() will filter None values and merge onto parent context
        stack.enter_context(config_context(overlay_instance))

        return stack

    def _on_nested_parameter_changed(self, param_name: str, value: Any) -> None:
        """
        Handle parameter changes from nested forms.

        When a nested form's field changes:
        1. Refresh parent form's placeholders (in case they inherit from nested values)
        2. Refresh all sibling nested forms' placeholders
        """
        # Refresh parent form's placeholders
        self._refresh_all_placeholders()

        # Refresh all nested managers' placeholders (including siblings)
        self._apply_to_nested_managers(lambda name, manager: manager._refresh_all_placeholders())

    def _refresh_all_placeholders(self) -> None:
        """Refresh placeholder text for all widgets in this form."""
        with timer(f"_refresh_all_placeholders ({self.field_id})", threshold_ms=5.0):
            # Allow placeholder refresh for nested forms even if they're not detected as lazy dataclasses
            # The placeholder service will determine if placeholders are available
            if not self.dataclass_type:
                return

            # Build overlay from current form state
            with timer("  get_current_values", threshold_ms=2.0):
                overlay = self.get_current_values()

            # Build context stack: parent context + overlay
            with self._build_context_stack(overlay):
                monitor = get_monitor("Placeholder resolution per field")
                for param_name, widget in self.widgets.items():
                    # CRITICAL: Check current value from overlay (live form state), not stale self.parameters
                    current_value = overlay.get(param_name) if isinstance(overlay, dict) else getattr(overlay, param_name, None)
                    if current_value is None:
                        with monitor.measure():
                            placeholder_text = self.service.get_placeholder_text(param_name, self.dataclass_type)
                            if placeholder_text:
                                from openhcs.pyqt_gui.widgets.shared.widget_strategies import PyQt6WidgetEnhancer
                                PyQt6WidgetEnhancer.apply_placeholder_text(widget, placeholder_text)

    def _apply_to_nested_managers(self, operation_func: callable) -> None:
        """Apply operation to all nested managers."""
        for param_name, nested_manager in self.nested_managers.items():
            operation_func(param_name, nested_manager)

    def _process_nested_values_if_checkbox_enabled(self, name: str, manager: Any, current_values: Dict[str, Any]) -> None:
        """Process nested values if checkbox is enabled - convert dict back to dataclass."""
        if not hasattr(manager, 'get_current_values'):
            return

        # Check if this is an Optional dataclass with a checkbox
        param_type = self.parameter_types.get(name)
        from openhcs.ui.shared.parameter_type_utils import ParameterTypeUtils

        if param_type and ParameterTypeUtils.is_optional_dataclass(param_type):
            # For Optional dataclasses, check if checkbox is enabled
            checkbox_widget = self.widgets.get(name)
            if checkbox_widget and hasattr(checkbox_widget, 'findChild'):
                from PyQt6.QtWidgets import QCheckBox
                checkbox = checkbox_widget.findChild(QCheckBox)
                if checkbox and not checkbox.isChecked():
                    # Checkbox is unchecked, set to None
                    current_values[name] = None
                    return

        # Get nested values from the nested form
        nested_values = manager.get_current_values()
        if nested_values:
            # Convert dictionary back to dataclass instance
            if param_type and hasattr(param_type, '__dataclass_fields__'):
                # Direct dataclass type
                current_values[name] = param_type(**nested_values)
            elif param_type and ParameterTypeUtils.is_optional_dataclass(param_type):
                # Optional dataclass type
                inner_type = ParameterTypeUtils.get_optional_inner_type(param_type)
                current_values[name] = inner_type(**nested_values)
            else:
                # Fallback to dictionary if type conversion fails
                current_values[name] = nested_values
        else:
            # No nested values, but checkbox might be checked - create empty instance
            if param_type and ParameterTypeUtils.is_optional_dataclass(param_type):
                inner_type = ParameterTypeUtils.get_optional_inner_type(param_type)
                current_values[name] = inner_type()  # Create with defaults

