"""
Napari-based real-time visualization module for OpenHCS.

This module provides the NapariStreamVisualizer class for real-time
visualization of tensors during pipeline execution.

Doctrinal Clauses:
- Clause 65 — No Fallback Logic
- Clause 66 — Immutability After Construction
- Clause 88 — No Inferred Capabilities
- Clause 368 — Visualization Must Be Observer-Only
"""

import logging
import multiprocessing
import os
import queue
import subprocess
import sys
import threading
import time
import zmq
import numpy as np
from typing import Any, Dict, Optional

from openhcs.io.filemanager import FileManager
from openhcs.utils.import_utils import optional_import
from openhcs.constants.constants import DEFAULT_NAPARI_STREAM_PORT

# Optional napari import - this module should only be imported if napari is available
napari = optional_import("napari")
if napari is None:
    raise ImportError(
        "napari is required for NapariStreamVisualizer. "
        "Install it with: pip install 'openhcs[viz]' or pip install napari"
    )

import numpy as np

logger = logging.getLogger(__name__)

# Global process management for napari viewer
_global_viewer_process: Optional[multiprocessing.Process] = None
_global_viewer_port: Optional[int] = None
_global_process_lock = threading.Lock()


def _cleanup_global_viewer() -> None:
    """
    Clean up global napari viewer process for test mode.

    This forcibly terminates the napari viewer process to allow pytest to exit.
    Should only be called in test mode.
    """
    global _global_viewer_process

    with _global_process_lock:
        if _global_viewer_process and _global_viewer_process.is_alive():
            logger.info("🔬 VISUALIZER: Terminating napari viewer for test cleanup")
            _global_viewer_process.terminate()
            _global_viewer_process.join(timeout=3)

            if _global_viewer_process.is_alive():
                logger.warning("🔬 VISUALIZER: Force killing napari viewer process")
                _global_viewer_process.kill()
                _global_viewer_process.join(timeout=1)

            _global_viewer_process = None


def _parse_component_info_from_path(path_str: str):
    """
    Fallback component parsing from path (used when component metadata unavailable).

    Args:
        path_str: Path string like 'step_name/A01/s1_c2_z3.tif'

    Returns:
        Dict with basic component info extracted from filename
    """
    try:
        import os
        import re
        filename = os.path.basename(path_str)

        # Basic regex for common patterns
        pattern = r'(?:s(\d+))?(?:_c(\d+))?(?:_z(\d+))?'
        match = re.search(pattern, filename)

        components = {}
        if match:
            site, channel, z_index = match.groups()
            if site:
                components['site'] = site
            if channel:
                components['channel'] = channel
            if z_index:
                components['z_index'] = z_index

        return components
    except Exception:
        return {}


def _handle_component_aware_display(viewer, layers, component_groups, image_data, path,
                                   colormap, display_config, replace_layers, component_metadata=None):
    """
    Handle component-aware display following OpenHCS stacking patterns.

    Creates separate layers for each step and well, with proper component-based stacking.
    Each step gets its own layer. Each well gets its own layer. Components marked as
    SLICE create separate layers, components marked as STACK are stacked together.
    """
    try:
        # Use component metadata from ZMQ message - fail loud if not available
        if not component_metadata:
            raise ValueError(f"No component metadata available for path: {path}")
        component_info = component_metadata

        # Get step information from component metadata
        step_index = component_info.get('step_index', 0)
        step_name = component_info.get('step_name', 'unknown_step')

        # Create step prefix for layer naming
        step_prefix = f"step_{step_index:02d}_{step_name}"

        # Get well identifier (configurable: slice vs stack)
        well_id = component_info.get('well', 'unknown_well')

        # Build component_modes from config (dict or object), default to channel=slice, others=stack
        component_modes = None
        if isinstance(display_config, dict):
            cm = display_config.get('component_modes') or display_config.get('componentModes')
            if isinstance(cm, dict) and cm:
                component_modes = cm
        if component_modes is None:
            # Handle object-like config (NapariDisplayConfig)
            component_modes = {}
            for component in ['site', 'channel', 'z_index', 'well']:
                mode_field = f"{component}_mode"
                if hasattr(display_config, mode_field):
                    mode_value = getattr(display_config, mode_field)
                    component_modes[component] = getattr(mode_value, 'value', str(mode_value))
                else:
                    component_modes[component] = 'slice' if component == 'channel' else 'stack'

        # Create layer grouping key: step_prefix + optionally well + slice_components
        # Each unique combination gets its own layer
        layer_key_parts = [step_prefix]
        if component_modes.get('well', 'stack') == 'slice':
            layer_key_parts.append(well_id)

        # Add slice components to layer key (these create separate layers)
        for component_name, mode in component_modes.items():
            if mode == 'slice' and component_name in component_info and component_name != 'well':
                layer_key_parts.append(f"{component_name}_{component_info[component_name]}")

        layer_key = "_".join(layer_key_parts)

        # Reconcile cached layer/group state with live napari viewer after possible manual deletions
        try:
            current_layer_names = {l.name for l in viewer.layers}
            if layer_key not in current_layer_names:
                # Drop any stale references so we will recreate the layer
                layers.pop(layer_key, None)
                component_groups.pop(layer_key, None)
                logger.debug(f"🔬 NAPARI PROCESS: Reconciling state — '{layer_key}' not in viewer; purged stale caches")
        except Exception:
            # Fail-loud elsewhere; reconciliation is best-effort and must not mask display
            pass

        # Initialize layer group if needed
        if layer_key not in component_groups:
            component_groups[layer_key] = []

        # Add image to layer group
        component_groups[layer_key].append({
            'data': image_data,
            'components': component_info,
            'path': str(path)
        })

        # Get all images for this layer
        layer_images = component_groups[layer_key]

        # Determine if we should stack or use single image
        stack_components = [comp for comp, mode in component_modes.items()
                          if mode == 'stack' and comp in component_info]

        if len(layer_images) == 1:
            # Single image - add directly
            layer_name = layer_key

            # Check if layer exists in actual napari viewer
            existing_layer = None
            for layer in viewer.layers:
                if layer.name == layer_name:
                    existing_layer = layer
                    break

            if existing_layer is not None:
                # Update existing layer
                existing_layer.data = image_data
                layers[layer_name] = existing_layer
                logger.info(f"🔬 NAPARI PROCESS: Updated existing layer {layer_name}")
            else:
                # Create new layer - this should always work for new names
                logger.info(f"🔬 NAPARI PROCESS: Creating new layer {layer_name}, viewer has {len(viewer.layers)} existing layers")
                logger.info(f"🔬 NAPARI PROCESS: Existing layer names: {[layer.name for layer in viewer.layers]}")
                logger.info(f"🔬 NAPARI PROCESS: Image data shape: {image_data.shape}, dtype: {image_data.dtype}")
                logger.info(f"🔬 NAPARI PROCESS: Viewer type: {type(viewer)}")
                try:
                    new_layer = viewer.add_image(image_data, name=layer_name, colormap=colormap)
                    layers[layer_name] = new_layer
                    logger.info(f"🔬 NAPARI PROCESS: Successfully created new layer {layer_name}")
                    logger.info(f"🔬 NAPARI PROCESS: Viewer now has {len(viewer.layers)} layers")
                except Exception as e:
                    logger.error(f"🔬 NAPARI PROCESS: FAILED to create layer {layer_name}: {e}")
                    logger.error(f"🔬 NAPARI PROCESS: Exception type: {type(e)}")
                    import traceback
                    logger.error(f"🔬 NAPARI PROCESS: Traceback: {traceback.format_exc()}")
                    raise
        else:
            # Multiple images - create multi-dimensional array for napari
            try:
                # Sort images by stack components for consistent ordering
                if stack_components:
                    def sort_key(img_info):
                        return tuple(img_info['components'].get(comp, 0) for comp in stack_components)
                    layer_images.sort(key=sort_key)

                # Group images by stack component values to create proper dimensions
                if len(stack_components) == 1:
                    # Single stack component - simple 3D stack
                    image_stack = [img['data'] for img in layer_images]
                    from openhcs.core.memory.stack_utils import stack_slices
                    stacked_data = stack_slices(image_stack, memory_type='numpy', gpu_id=0)
                else:
                    # Multiple stack components - create multi-dimensional array
                    # Get unique values for each stack component
                    component_values = {}
                    for comp in stack_components:
                        values = sorted(set(img['components'].get(comp, 0) for img in layer_images))
                        component_values[comp] = values

                    # Create multi-dimensional array
                    # Shape: (comp1_size, comp2_size, ..., height, width)
                    shape_dims = [len(component_values[comp]) for comp in stack_components]
                    first_img = layer_images[0]['data']
                    full_shape = tuple(shape_dims + list(first_img.shape))
                    stacked_data = np.zeros(full_shape, dtype=first_img.dtype)

                    # Fill the multi-dimensional array
                    for img_info in layer_images:
                        # Get indices for this image
                        indices = []
                        for comp in stack_components:
                            comp_value = img_info['components'].get(comp, 0)
                            comp_index = component_values[comp].index(comp_value)
                            indices.append(comp_index)

                        # Place image in the correct position
                        stacked_data[tuple(indices)] = img_info['data']

                # Update or create stack layer
                layer_name = layer_key

                # Check if layer exists in actual napari viewer
                existing_layer = None
                for layer in viewer.layers:
                    if layer.name == layer_name:
                        existing_layer = layer
                        break

                if existing_layer is not None:
                    # Update existing layer
                    existing_layer.data = stacked_data
                    layers[layer_name] = existing_layer
                    logger.info(f"🔬 NAPARI PROCESS: Updated existing stack layer {layer_name} (shape: {stacked_data.shape})")
                else:
                    # Create new layer - this should always work for new names
                    logger.info(f"🔬 NAPARI PROCESS: Creating new stack layer {layer_name}, viewer has {len(viewer.layers)} existing layers")
                    try:
                        new_layer = viewer.add_image(stacked_data, name=layer_name, colormap=colormap)
                        layers[layer_name] = new_layer
                        logger.info(f"🔬 NAPARI PROCESS: Successfully created new stack layer {layer_name} (shape: {stacked_data.shape})")
                    except Exception as e:
                        logger.error(f"🔬 NAPARI PROCESS: FAILED to create stack layer {layer_name}: {e}")
                        import traceback
                        logger.error(f"🔬 NAPARI PROCESS: Traceback: {traceback.format_exc()}")
                        raise

            except Exception as e:
                logger.error(f"🔬 NAPARI PROCESS: Failed to create stack for layer {layer_key}: {e}")
                import traceback
                logger.error(f"🔬 NAPARI PROCESS: Traceback: {traceback.format_exc()}")
                raise

    except Exception as e:
        import traceback
        logger.error(f"🔬 NAPARI PROCESS: Component-aware display failed for {path}: {e}")
        logger.error(f"🔬 NAPARI PROCESS: Component-aware display traceback: {traceback.format_exc()}")
        raise  # Fail loud - no fallback


def _napari_viewer_process(port: int, viewer_title: str, replace_layers: bool = False):
    """
    Napari viewer process entry point. Runs in a separate process.
    Listens for ZeroMQ messages with image data to display.

    Args:
        port: ZMQ port to listen on
        viewer_title: Title for the napari viewer window
        replace_layers: If True, replace existing layers; if False, add new layers with unique names
    """
    try:
        import zmq
        import napari
        import numpy as np
        import pickle

        # Set up ZeroMQ communication
        context = zmq.Context()

        # Data channel: SUB socket for receiving images
        data_socket = context.socket(zmq.SUB)
        data_socket.bind(f"tcp://*:{port}")
        data_socket.setsockopt(zmq.SUBSCRIBE, b"")  # Subscribe to all messages

        # Control channel: REP socket for handshake
        control_port = port + 1000  # Use port+1000 for control
        control_socket = context.socket(zmq.REP)
        control_socket.bind(f"tcp://*:{control_port}")

        # Create napari viewer in this process (main thread)
        viewer = napari.Viewer(title=viewer_title, show=True)

        # Initialize layers dictionary with existing layers (for reconnection scenarios)
        layers = {}
        for layer in viewer.layers:
            layers[layer.name] = layer

        napari_ready = False  # Track readiness state

        # Component grouping for stacking (following OpenHCS pattern)
        component_groups = {}  # {component_type: {group_key: [images]}}
        display_config = None  # Store display config for component mode decisions

        logger.info(f"🔬 NAPARI PROCESS: Viewer started on data port {port}, control port {control_port}")

        # Add cleanup handler for when viewer is closed
        def cleanup_and_exit():
            logger.info("🔬 NAPARI PROCESS: Viewer closed, cleaning up and exiting...")
            try:
                data_socket.close()
                control_socket.close()
                context.term()
            except:
                pass
            sys.exit(0)

        # Connect the viewer close event to cleanup
        viewer.window.qt_viewer.destroyed.connect(cleanup_and_exit)

        # Use proper Qt event loop integration
        import sys
        from qtpy import QtWidgets, QtCore

        # Ensure Qt platform is properly set for detached processes
        import os
        if 'QT_QPA_PLATFORM' not in os.environ:
            os.environ['QT_QPA_PLATFORM'] = 'xcb'

        # Disable shared memory for X11 (helps with display issues in detached processes)
        os.environ['QT_X11_NO_MITSHM'] = '1'

        # Get the Qt application
        app = QtWidgets.QApplication.instance()
        if app is None:
            app = QtWidgets.QApplication(sys.argv)

        # Ensure the application DOES quit when the napari window closes
        app.setQuitOnLastWindowClosed(True)

        # Set up a QTimer for message processing
        timer = QtCore.QTimer()

        def process_messages():
            nonlocal napari_ready
            # Handle control messages (handshake) first
            try:
                control_message = control_socket.recv(zmq.NOBLOCK)
                control_data = pickle.loads(control_message)

                if control_data.get('type') == 'ping':
                    # Client is checking if we're ready
                    if not napari_ready:
                        # Mark as ready after first ping (GUI should be loaded by now)
                        napari_ready = True
                        logger.info(f"🔬 NAPARI PROCESS: Marked as ready after ping")

                    response = {'type': 'pong', 'ready': napari_ready}
                    control_socket.send(pickle.dumps(response))
                    logger.debug(f"🔬 NAPARI PROCESS: Responded to ping with ready={napari_ready}")

            except zmq.Again:
                pass  # No control messages

            # Debug: Print current layer count (only when layers change)
            # Removed continuous debug printing to avoid terminal spam

            # Process data messages only if ready
            if napari_ready:
                # Process multiple messages per timer tick for better throughput
                for _ in range(10):  # Process up to 10 messages per tick
                    try:
                        message = data_socket.recv(zmq.NOBLOCK)

                        # Try to parse as JSON first (from NapariStreamingBackend)
                        import json
                        data = json.loads(message.decode('utf-8'))

                        # Check if this is a batch message
                        if data.get('type') == 'batch':
                            # Handle batch of images
                            images = data.get('images', [])
                            display_config_dict = data.get('display_config')

                            # Use display_config_dict directly - no need to store globally

                                # Process all images in the batch together
                            for image_info in images:
                                path = image_info.get('path', 'unknown')
                                shape = image_info.get('shape')
                                dtype = image_info.get('dtype')
                                shm_name = image_info.get('shm_name')
                                component_metadata = image_info.get('component_metadata', {})

                                # Add step information to component metadata
                                component_metadata['step_index'] = image_info.get('step_index', 0)
                                component_metadata['step_name'] = image_info.get('step_name', 'unknown_step')

                                # Load from shared memory
                                from multiprocessing import shared_memory
                                shm = shared_memory.SharedMemory(name=shm_name)
                                image_data = np.ndarray(shape, dtype=dtype, buffer=shm.buf).copy()
                                shm.close()  # Close our reference

                                # Extract colormap from display config
                                colormap = 'viridis'  # Default
                                if display_config_dict and 'colormap' in display_config_dict:
                                    colormap = display_config_dict['colormap']

                                # Component-aware layer management (following OpenHCS pattern)
                                _handle_component_aware_display(
                                    viewer, layers, component_groups, image_data, path,
                                    colormap, display_config_dict or {}, replace_layers, component_metadata
                                )
                        else:
                            # Handle single image format
                            path = data.get('path', 'unknown')
                            shape = data.get('shape')
                            dtype = data.get('dtype')
                            shm_name = data.get('shm_name')
                            direct_data = data.get('data')
                            display_config_dict = data.get('display_config')
                            component_metadata = data.get('component_metadata', {})

                            # Add step information to component metadata
                            component_metadata['step_index'] = data.get('step_index', 0)
                            component_metadata['step_name'] = data.get('step_name', 'unknown_step')

                            # Use display_config_dict directly - no need to store globally

                            if shm_name:
                                # Load from shared memory
                                from multiprocessing import shared_memory
                                shm = shared_memory.SharedMemory(name=shm_name)
                                image_data = np.ndarray(shape, dtype=dtype, buffer=shm.buf).copy()
                                shm.close()  # Close our reference
                            elif direct_data:
                                # Load from direct data (fallback)
                                image_data = np.array(direct_data, dtype=dtype).reshape(shape)
                            else:
                                logger.warning(f"🔬 NAPARI PROCESS: No image data in message")
                                continue

                            # Extract colormap from display config
                            colormap = 'viridis'  # Default
                            if display_config_dict and 'colormap' in display_config_dict:
                                colormap = display_config_dict['colormap']

                            # Component-aware layer management (following OpenHCS pattern)
                            _handle_component_aware_display(
                                viewer, layers, component_groups, image_data, path,
                                colormap, display_config_dict or {}, replace_layers, component_metadata
                            )



                    except zmq.Again:
                        # No more messages available
                        break



        # Connect timer to message processing
        timer.timeout.connect(process_messages)
        timer.start(50)  # Process messages every 50ms

        logger.info("🔬 NAPARI PROCESS: Starting Qt event loop")

        # Run the Qt event loop - this keeps napari responsive
        app.exec_()

    except Exception as e:
        logger.error(f"🔬 NAPARI PROCESS: Fatal error: {e}")
    finally:
        logger.info("🔬 NAPARI PROCESS: Shutting down")
        if 'socket' in locals():
            socket.close()
        if 'context' in locals():
            context.term()


def _spawn_detached_napari_process(port: int, viewer_title: str, replace_layers: bool = False) -> subprocess.Popen:
    """
    Spawn a completely detached napari viewer process that survives parent termination.

    This creates a subprocess that runs independently and won't be terminated when
    the parent process exits, enabling true persistence across pipeline runs.
    """
    # Use a simpler approach: spawn python directly with the napari viewer module
    # This avoids temporary file issues and import problems

    # Create the command to run the napari viewer directly
    current_dir = os.getcwd()
    python_code = f'''
import sys
import os

# Detach from parent process group (Unix only)
if hasattr(os, "setsid"):
    try:
        os.setsid()
    except OSError:
        pass

# Add current working directory to Python path
sys.path.insert(0, "{current_dir}")

try:
    from openhcs.runtime.napari_stream_visualizer import _napari_viewer_process
    _napari_viewer_process({port}, "{viewer_title}", {replace_layers})
except Exception as e:
    import logging
    logger = logging.getLogger("openhcs.runtime.napari_detached")
    logger.error(f"Detached napari error: {{e}}")
    import traceback
    logger.error(traceback.format_exc())
    sys.exit(1)
'''

    try:
        # Use subprocess.Popen with detachment flags
        if sys.platform == "win32":
            # Windows: Use CREATE_NEW_PROCESS_GROUP to detach but preserve display environment
            env = os.environ.copy()  # Preserve environment variables
            process = subprocess.Popen(
                [sys.executable, "-c", python_code],
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
                env=env,
                cwd=os.getcwd()
                # Don't redirect stdout/stderr to allow GUI to display properly
            )
        else:
            # Unix: Use start_new_session to detach but preserve display environment
            env = os.environ.copy()  # Preserve DISPLAY and other environment variables

            # Ensure Qt platform is set for GUI display
            if 'QT_QPA_PLATFORM' not in env:
                env['QT_QPA_PLATFORM'] = 'xcb'  # Use X11 backend

            # Ensure Qt can find the display
            env['QT_X11_NO_MITSHM'] = '1'  # Disable shared memory for X11 (helps with some display issues)

            # Try without start_new_session to see if GUI displays properly
            process = subprocess.Popen(
                [sys.executable, "-c", python_code],
                env=env,
                cwd=os.getcwd()
                # Don't redirect stdout/stderr to allow GUI to display properly
            )

        logger.info(f"🔬 VISUALIZER: Detached napari process started (PID: {process.pid})")
        return process

    except Exception as e:
        logger.error(f"🔬 VISUALIZER: Failed to spawn detached napari process: {e}")
        raise e


class NapariStreamVisualizer:
    """
    Manages a Napari viewer instance for real-time visualization of tensors
    streamed from the OpenHCS pipeline. Runs napari in a separate process
    for Qt compatibility and true persistence across pipeline runs.
    """

    def __init__(self, filemanager: FileManager, visualizer_config, viewer_title: str = "OpenHCS Real-Time Visualization", persistent: bool = True, napari_port: int = DEFAULT_NAPARI_STREAM_PORT, replace_layers: bool = False, display_config=None):
        self.filemanager = filemanager
        self.viewer_title = viewer_title
        self.persistent = persistent  # If True, viewer process stays alive after pipeline completion
        self.visualizer_config = visualizer_config
        self.napari_port = napari_port  # Port for napari streaming
        self.replace_layers = replace_layers  # If True, replace existing layers; if False, add new layers
        self.display_config = display_config  # Configuration for display behavior
        self.port: Optional[int] = None
        self.process: Optional[multiprocessing.Process] = None
        self.zmq_context: Optional[zmq.Context] = None
        self.zmq_socket: Optional[zmq.Socket] = None
        self.is_running = False
        self._lock = threading.Lock()

        # Clause 368: Visualization must be observer-only.
        # This class will only read data and display it.

    def _find_free_port(self) -> int:
        """Find a free port for ZeroMQ communication."""
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            return s.getsockname()[1]

    def start_viewer(self):
        """Starts the Napari viewer in a separate process."""
        global _global_viewer_process, _global_viewer_port

        with self._lock:
            # Check if there's already a napari viewer running on the configured port
            port_in_use = self._is_port_in_use(self.napari_port)
            logger.info(f"🔬 VISUALIZER: Port {self.napari_port} in use: {port_in_use}")
            if port_in_use:
                logger.info(f"🔬 VISUALIZER: Reusing existing napari viewer on port {self.napari_port}")
                # Set the port and connect to existing viewer
                self.port = self.napari_port

                # Check if we have a reference to the global process
                with _global_process_lock:
                    if _global_viewer_process and _global_viewer_port == self.napari_port:
                        self.process = _global_viewer_process
                        logger.info(f"🔬 VISUALIZER: Found global process reference (PID: {self.process.pid})")
                    else:
                        self.process = None  # External process we don't control
                        logger.info("🔬 VISUALIZER: No global process reference (external viewer)")

                self._setup_zmq_client()
                self.is_running = True
                return

            if self.is_running:
                logger.warning("Napari viewer is already running.")
                return

            # Use configured port for napari streaming
            self.port = self.napari_port
            logger.info(f"🔬 VISUALIZER: Starting napari viewer process on port {self.port}")

            if self.persistent:
                # For persistent viewers, use detached subprocess that truly survives parent termination
                logger.info("🔬 VISUALIZER: Creating detached persistent napari viewer")
                self.process = _spawn_detached_napari_process(self.port, self.viewer_title, self.replace_layers)
            else:
                # For non-persistent viewers, use multiprocessing.Process
                logger.info("🔬 VISUALIZER: Creating non-persistent napari viewer")
                self.process = multiprocessing.Process(
                    target=_napari_viewer_process,
                    args=(self.port, self.viewer_title, self.replace_layers),
                    daemon=False
                )
                self.process.start()

            # Update global references
            with _global_process_lock:
                _global_viewer_process = self.process
                _global_viewer_port = self.port

            # Wait for napari viewer to be ready before setting up ZMQ
            self._wait_for_viewer_ready()

            # Set up ZeroMQ client
            self._setup_zmq_client()

            # Check if process is running (different methods for subprocess vs multiprocessing)
            if hasattr(self.process, 'is_alive'):
                # multiprocessing.Process
                process_alive = self.process.is_alive()
            else:
                # subprocess.Popen
                process_alive = self.process.poll() is None

            if process_alive:
                self.is_running = True
                logger.info(f"🔬 VISUALIZER: Napari viewer process started successfully (PID: {self.process.pid})")
            else:
                logger.error("🔬 VISUALIZER: Failed to start napari viewer process")

    def _try_connect_to_existing_viewer(self, port: int) -> bool:
        """Try to connect to an existing napari viewer on the given port."""
        import socket

        # First check if anything is listening on the port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)  # 100ms timeout
        try:
            result = sock.connect_ex(('localhost', port))
            sock.close()

            if result == 0:  # Port is open
                # Set up ZMQ connection
                self._setup_zmq_client()
                return True
            else:
                return False

        except Exception:
            return False

    def _is_port_in_use(self, port: int) -> bool:
        """Check if a port is already in use (indicating existing napari viewer)."""
        import socket

        # Check if any process is listening on this port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        try:
            # Try to bind to the port - if it fails, something is already using it
            sock.bind(('localhost', port))
            sock.close()
            return False  # Port is free
        except OSError:
            # Port is already in use
            sock.close()
            return True
        except Exception:
            return False

    def _wait_for_viewer_ready(self, timeout: float = 10.0) -> bool:
        """Wait for the napari viewer to be ready using handshake protocol."""
        import zmq

        logger.info(f"🔬 VISUALIZER: Waiting for napari viewer to be ready on port {self.port}...")

        # First wait for ports to be bound
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self._is_port_in_use(self.port) and self._is_port_in_use(self.port + 1000):
                break
            time.sleep(0.2)
        else:
            logger.warning(f"🔬 VISUALIZER: Timeout waiting for ports to be bound")
            return False

        # Now use handshake protocol - create fresh socket for each attempt
        start_time = time.time()
        while time.time() - start_time < timeout:
            control_context = zmq.Context()
            control_socket = control_context.socket(zmq.REQ)
            control_socket.setsockopt(zmq.LINGER, 0)
            control_socket.setsockopt(zmq.RCVTIMEO, 1000)  # 1 second timeout

            try:
                control_socket.connect(f"tcp://localhost:{self.port + 1000}")

                import pickle
                ping_message = {'type': 'ping'}
                control_socket.send(pickle.dumps(ping_message))

                response = control_socket.recv()
                response_data = pickle.loads(response)

                if response_data.get('type') == 'pong' and response_data.get('ready'):
                    logger.info(f"🔬 VISUALIZER: Napari viewer is ready on port {self.port}")
                    return True

            except zmq.Again:
                pass  # Timeout waiting for response
            except Exception as e:
                logger.debug(f"🔬 VISUALIZER: Handshake attempt failed: {e}")
            finally:
                control_socket.close()
                control_context.term()

            time.sleep(0.5)  # Wait before next ping

        logger.warning(f"🔬 VISUALIZER: Timeout waiting for napari viewer handshake")
        return False

    def _setup_zmq_client(self):
        """Set up ZeroMQ client to send data to viewer process."""
        if self.port is None:
            raise RuntimeError("Port not set - call start_viewer() first")

        self.zmq_context = zmq.Context()
        self.zmq_socket = self.zmq_context.socket(zmq.PUB)
        self.zmq_socket.connect(f"tcp://localhost:{self.port}")

        # Brief delay for ZMQ connection to establish
        time.sleep(0.1)
        logger.info(f"🔬 VISUALIZER: ZMQ client connected to port {self.port}")

    def send_image_data(self, step_id: str, image_data: np.ndarray, axis_id: str = "unknown"):
        """
        DISABLED: This method bypasses component-aware stacking.
        All visualization must go through the streaming backend.
        """
        raise RuntimeError(
            f"send_image_data() is disabled. Use streaming backend for component-aware display. "
            f"step_id: {step_id}, axis_id: {axis_id}, shape: {image_data.shape}"
        )

    def stop_viewer(self):
        """Stop the napari viewer process (only if not persistent)."""
        with self._lock:
            if not self.persistent:
                logger.info("🔬 VISUALIZER: Stopping non-persistent napari viewer")
                self._cleanup_zmq()
                if self.process:
                    # Handle both subprocess and multiprocessing process types
                    if hasattr(self.process, 'is_alive'):
                        # multiprocessing.Process
                        if self.process.is_alive():
                            self.process.terminate()
                            self.process.join(timeout=5)
                            if self.process.is_alive():
                                logger.warning("🔬 VISUALIZER: Force killing napari viewer process")
                                self.process.kill()
                    else:
                        # subprocess.Popen
                        if self.process.poll() is None:  # Still running
                            self.process.terminate()
                            try:
                                self.process.wait(timeout=5)
                            except subprocess.TimeoutExpired:
                                logger.warning("🔬 VISUALIZER: Force killing napari viewer process")
                                self.process.kill()
                self.is_running = False
            else:
                logger.info("🔬 VISUALIZER: Keeping persistent napari viewer alive")
                # Just cleanup our ZMQ connection, leave process running
                self._cleanup_zmq()
                # DON'T set is_running = False for persistent viewers!
                # The process is still alive and should be reusable

    def _cleanup_zmq(self):
        """Clean up ZeroMQ resources."""
        if self.zmq_socket:
            self.zmq_socket.close()
            self.zmq_socket = None
        if self.zmq_context:
            self.zmq_context.term()
            self.zmq_context = None

    def visualize_path(self, step_id: str, path: str, backend: str, axis_id: Optional[str] = None):
        """
        DISABLED: This method bypasses component-aware stacking.
        All visualization must go through the streaming backend.
        """
        raise RuntimeError(
            f"visualize_path() is disabled. Use streaming backend for component-aware display. "
            f"Path: {path}, step_id: {step_id}, axis_id: {axis_id}"
        )

    def _prepare_data_for_display(self, data: Any, step_id_for_log: str, display_config=None) -> Optional[np.ndarray]:
        """Converts loaded data to a displayable NumPy array (slice or stack based on config)."""
        cpu_tensor: Optional[np.ndarray] = None
        try:
            # GPU to CPU conversion logic
            if hasattr(data, 'is_cuda') and data.is_cuda:  # PyTorch
                cpu_tensor = data.cpu().numpy()
            elif hasattr(data, 'device') and 'cuda' in str(data.device).lower():  # Check for device attribute
                if hasattr(data, 'get'):  # CuPy
                    cpu_tensor = data.get()
                elif hasattr(data, 'numpy'): # JAX on GPU might have .numpy() after host transfer
                    cpu_tensor = np.asarray(data) # JAX arrays might need explicit conversion
                else: # Fallback for other GPU array types if possible
                    logger.warning(f"Unknown GPU array type for step '{step_id_for_log}'. Attempting .numpy().")
                    if hasattr(data, 'numpy'):
                        cpu_tensor = data.numpy()
                    else:
                        logger.error(f"Cannot convert GPU tensor of type {type(data)} for step '{step_id_for_log}'.")
                        return None
            elif isinstance(data, np.ndarray):
                cpu_tensor = data
            else:
                # Attempt to convert to numpy array if it's some other array-like structure
                try:
                    cpu_tensor = np.asarray(data)
                    logger.debug(f"Converted data of type {type(data)} to numpy array for step '{step_id_for_log}'.")
                except Exception as e_conv:
                    logger.warning(f"Unsupported data type for step '{step_id_for_log}': {type(data)}. Error: {e_conv}")
                    return None

            if cpu_tensor is None: # Should not happen if logic above is correct
                return None

            # Determine display mode based on configuration
            # Default behavior: show as stack unless config specifies otherwise
            should_slice = False

            if display_config:
                # Check if any component mode is set to SLICE
                from openhcs.core.config import NapariDimensionMode
                from openhcs.constants import VariableComponents

                # Check individual component mode fields
                for component in VariableComponents:
                    field_name = f"{component.value}_mode"
                    if hasattr(display_config, field_name):
                        mode = getattr(display_config, field_name)
                        if mode == NapariDimensionMode.SLICE:
                            should_slice = True
                            break
            else:
                # Default: slice for backward compatibility
                should_slice = True

            # Slicing/stacking logic
            display_data: Optional[np.ndarray] = None

            if should_slice:
                # Original slicing behavior
                if cpu_tensor.ndim == 3: # ZYX
                    display_data = cpu_tensor[cpu_tensor.shape[0] // 2, :, :]
                elif cpu_tensor.ndim == 2: # YX
                    display_data = cpu_tensor
                elif cpu_tensor.ndim > 3: # e.g. CZYX or TZYX
                    logger.debug(f"Tensor for step '{step_id_for_log}' has ndim > 3 ({cpu_tensor.ndim}). Taking a slice.")
                    slicer = [0] * (cpu_tensor.ndim - 2) # Slice first channels/times
                    slicer[-1] = cpu_tensor.shape[-3] // 2 # Middle Z
                    try:
                        display_data = cpu_tensor[tuple(slicer)]
                    except IndexError: # Handle cases where slicing might fail (e.g. very small dimensions)
                        logger.error(f"Slicing failed for tensor with shape {cpu_tensor.shape} for step '{step_id_for_log}'.", exc_info=True)
                        display_data = None
                else:
                    logger.warning(f"Tensor for step '{step_id_for_log}' has unsupported ndim for slicing: {cpu_tensor.ndim}.")
                    return None
            else:
                # Stack mode: send the full data to napari (napari can handle 3D+ data)
                if cpu_tensor.ndim >= 2:
                    display_data = cpu_tensor
                    logger.debug(f"Sending {cpu_tensor.ndim}D stack to napari for step '{step_id_for_log}' (shape: {cpu_tensor.shape})")
                else:
                    logger.warning(f"Tensor for step '{step_id_for_log}' has unsupported ndim for stacking: {cpu_tensor.ndim}.")
                    return None

            return display_data.copy() if display_data is not None else None

        except Exception as e:
            logger.error(f"Error preparing data from step '{step_id_for_log}' for display: {e}", exc_info=True)
            return None

