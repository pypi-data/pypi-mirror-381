"""Modern async JoyCon driver for Python 3.13+."""

from ajoycon.async_events import ButtonEvent, ButtonEventJoyCon, JoyConButtonEvent
from ajoycon.async_gyro import GyroTrackingJoyCon, Rotation
from ajoycon.async_joycon import AsyncJoyCon, JoyConError, connect_joycon
from ajoycon.discovery import JoyConDevice, JoyConType, discover_joycons
from ajoycon.models import (
    Acceleration,
    Battery,
    BatteryLevel,
    Buttons,
    Gyroscope,
    IMUData,
    JoyConStatus,
)

__version__ = "1.0.0"

__all__ = [
    "AsyncJoyCon",
    "ButtonEvent",
    "ButtonEventJoyCon",
    "GyroTrackingJoyCon",
    "JoyConButtonEvent",
    "JoyConDevice",
    "JoyConError",
    "JoyConType",
    "Rotation",
    "connect_joycon",
    "discover_joycons",
    "Acceleration",
    "Battery",
    "BatteryLevel",
    "Buttons",
    "Gyroscope",
    "IMUData",
    "JoyConStatus",
]
