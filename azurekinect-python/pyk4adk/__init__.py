from .pyk4adk import *

# k4a module
from .k4a import (
    Calibration, 
    Capture, 
    Configuration, 
    default_configuration, 
    Device, 
    Image, 
    ImuSample, 
    Transformation,
)
from .k4a._k4atypes import *

# k4record module
from .k4arecord import (
    Datablock, 
    Record, 
    Playback,
)

# pyk4a module
from .pyk4a.calibration import Calibration, CalibrationType
from .pyk4a.capture import PyK4ACapture
from .pyk4a.config import (
    FPS,
    ColorControlCommand,
    ColorControlMode,
    ColorResolution,
    Config,
    DepthMode,
    ImageFormat,
    WiredSyncMode,
)
from .pyk4a.errors import K4AException, K4ATimeoutException
from .pyk4a.module import k4a_module
from .pyk4a.playback import PyK4APlayback, SeekOrigin
from .pyk4a import ColorControlCapabilities, PyK4A
from .pyk4a.record import PyK4ARecord
from .pyk4a.transformation import (
    color_image_to_depth_camera,
    depth_image_to_color_camera,
    depth_image_to_color_camera_custom,
    depth_image_to_point_cloud,
)


def connected_device_count() -> int:
    return k4a_module.device_get_installed_count()



__all__ = (
    "Calibration",
    "CalibrationType",
    "FPS",
    "ColorControlCommand",
    "ColorControlMode",
    "ImageFormat",
    "ColorResolution",
    "Config",
    "DepthMode",
    "WiredSyncMode",
    "K4AException",
    "K4ATimeoutException",
    "PyK4A",
    "PyK4ACapture",
    "PyK4APlayback",
    "SeekOrigin",
    "ColorControlCapabilities",
    "color_image_to_depth_camera",
    "depth_image_to_point_cloud",
    "depth_image_to_color_camera",
    "depth_image_to_color_camera_custom",
    "PyK4ARecord",
    "connected_device_count",
)
