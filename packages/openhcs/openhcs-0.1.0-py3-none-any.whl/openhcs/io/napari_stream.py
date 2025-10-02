"""
Napari streaming backend for real-time visualization during processing.

This module provides a storage backend that streams image data to a napari viewer
for real-time visualization during pipeline execution. Uses ZeroMQ for IPC
and shared memory for efficient data transfer.
"""

import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Union, Set
from os import PathLike
import os

import numpy as np

from openhcs.io.streaming import StreamingBackend
from openhcs.io.backend_registry import StorageBackendMeta
from openhcs.constants.constants import Backend
from openhcs.constants.constants import DEFAULT_NAPARI_STREAM_PORT

logger = logging.getLogger(__name__)


class NapariStreamingBackend(StreamingBackend, metaclass=StorageBackendMeta):
    """Napari streaming backend with automatic metaclass registration."""

    # Backend type from enum for registration
    _backend_type = Backend.NAPARI_STREAM.value
    """
    Napari streaming backend for real-time visualization.

    Streams image data to napari viewer using ZeroMQ.
    Connects to existing NapariStreamVisualizer process.
    Inherits from StreamingBackend - no file system operations.
    """

    def __init__(self):
        """Initialize the napari streaming backend."""
        self._publisher = None
        self._context = None
        self._shared_memory_blocks = {}

    def _get_publisher(self, napari_port: int):
        """Lazy initialization of ZeroMQ publisher."""
        if self._publisher is None:
            try:
                import zmq
                self._context = zmq.Context()
                self._publisher = self._context.socket(zmq.PUB)

                self._publisher.connect(f"tcp://localhost:{napari_port}")
                logger.info(f"Napari streaming publisher connected to viewer on port {napari_port}")

                # Small delay to ensure socket is ready
                time.sleep(0.1)

            except ImportError:
                logger.error("ZeroMQ not available - napari streaming disabled")
                raise RuntimeError("ZeroMQ required for napari streaming")

        return self._publisher



    def save(self, data: Any, file_path: Union[str, Path], **kwargs) -> None:
        """Stream single image to napari."""
        self.save_batch([data], [file_path], **kwargs)

    def save_batch(self, data_list: List[Any], file_paths: List[Union[str, Path]], **kwargs) -> None:
        """
        Stream multiple images to napari as a batch.

        Args:
            data_list: List of image data
            file_paths: List of path identifiers
            **kwargs: Additional metadata
        """


        if len(data_list) != len(file_paths):
            raise ValueError("data_list and file_paths must have the same length")

        try:
            publisher = self._get_publisher(kwargs['napari_port'])
            display_config = kwargs['display_config']
            microscope_handler = kwargs['microscope_handler']
            step_index = kwargs.get('step_index', 0)
            step_name = kwargs.get('step_name', 'unknown_step')
        except KeyError as e:
            raise

        # Prepare batch of images
        batch_images = []
        for data, file_path in zip(data_list, file_paths):
            # Convert to numpy
            if hasattr(data, 'cpu'):
                np_data = data.cpu().numpy()
            elif hasattr(data, 'get'):
                np_data = data.get()
            else:
                np_data = np.asarray(data)

            # Create shared memory
            from multiprocessing import shared_memory
            shm_name = f"napari_{id(data)}_{time.time_ns()}"
            shm = shared_memory.SharedMemory(create=True, size=np_data.nbytes, name=shm_name)
            shm_array = np.ndarray(np_data.shape, dtype=np_data.dtype, buffer=shm.buf)
            shm_array[:] = np_data[:]
            self._shared_memory_blocks[shm_name] = shm

            # Parse component metadata
            filename = os.path.basename(str(file_path))
            component_metadata = microscope_handler.parser.parse_filename(filename)

            batch_images.append({
                'path': str(file_path),
                'shape': np_data.shape,
                'dtype': str(np_data.dtype),
                'shm_name': shm_name,
                'component_metadata': component_metadata,
                'step_index': step_index,
                'step_name': step_name
            })

        # Build component modes
        from openhcs.constants import VariableComponents
        component_modes = {}
        for component in VariableComponents:
            field_name = f"{component.value}_mode"
            mode = getattr(display_config, field_name)
            component_modes[component.value] = mode.value


        # Include well if available on the display config (not always part of VariableComponents)
        if hasattr(display_config, 'well_mode'):
            component_modes['well'] = display_config.well_mode.value

        # Send batch message
        message = {
            'type': 'batch',
            'images': batch_images,
'display_config': {
                'colormap': display_config.get_colormap_name(),
                'component_modes': component_modes
            },
            'timestamp': time.time()
        }

        publisher.send_json(message)

    # REMOVED: All file system methods (load, load_batch, exists, list_files, delete, etc.)
    # These are no longer inherited - clean interface!

    def cleanup_connections(self) -> None:
        """Clean up ZeroMQ connections without affecting shared memory or napari window."""
        # Close publisher and context
        if self._publisher is not None:
            self._publisher.close()
            self._publisher = None

        if self._context is not None:
            self._context.term()
            self._context = None

        logger.debug("Napari streaming connections cleaned up")

    def cleanup(self) -> None:
        """Clean up shared memory blocks and close publisher.

        Note: This does NOT close the napari window - it should remain open
        for future test executions and user interaction.
        """
        # Clean up shared memory blocks
        for shm_name, shm in self._shared_memory_blocks.items():
            try:
                shm.close()
                shm.unlink()
            except Exception as e:
                logger.warning(f"Failed to cleanup shared memory {shm_name}: {e}")

        self._shared_memory_blocks.clear()

        # Clean up connections
        self.cleanup_connections()

        logger.debug("Napari streaming backend cleaned up (napari window remains open)")

    def __del__(self):
        """Cleanup on deletion."""
        self.cleanup()
