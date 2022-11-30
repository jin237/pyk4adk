import ctypes

from pyk4adk.k4a import Device, _k4a, default_configuration
from pyk4adk.k4arecord import _k4arecord
from pyk4adk.k4arecord.playback import Playback
from pyk4adk.utils import (
    get_k4a_module_path, get_k4arecord_module_path
)
from pyk4adk.pyk4a.pyk4a import (
    k4a_module, 
    PyK4APlayback, 
    SeekOrigin, 
    ColorControlCapabilities, 
    PyK4A,
    PyK4ARecord,
)
from pyk4adk.pyk4a.pyk4a.transformation import (
    color_image_to_depth_camera,
    depth_image_to_color_camera,
    depth_image_to_color_camera_custom,
    depth_image_to_point_cloud,
)


def initialize_libraries(module_k4a_path=None, module_k4abt_path=None, track_body=False):
    
    # Search the module path for k4a if not available
    if module_k4a_path is None:
        module_k4a_path = get_k4a_module_path()

    module_k4arecord_path = get_k4arecord_module_path(module_k4a_path)

    # Initialize k4a related wrappers
    init_k4a(module_k4a_path)

    # Initialize k4arecord related wrappers
    init_k4arecord(module_k4arecord_path)


def init_k4a(module_k4a_path):

    _k4a.setup_library(module_k4a_path)


def init_k4arecord(module_k4arecord_path):

    _k4arecord.setup_library(module_k4arecord_path)

def start_device(device_index=0, config=default_configuration, record=False, record_filepath="output.mkv"):
    
    # Create device object
    device = Device(device_index)

    # Start device
    device.start(config, record, record_filepath)

    return device

def start_playback(filepath):

    return Playback(filepath)

def connected_device_count() -> int:
    return k4a_module.device_get_installed_count()