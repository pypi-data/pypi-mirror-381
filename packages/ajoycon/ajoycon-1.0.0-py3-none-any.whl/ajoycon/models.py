"""Data models for JoyCon status."""

from dataclasses import dataclass
from enum import IntEnum
from typing import NamedTuple


class BatteryLevel(IntEnum):
    EMPTY = 0
    CRITICAL = 1
    LOW = 2
    MEDIUM = 3
    FULL = 4


@dataclass(frozen=True)
class Battery:
    charging: bool
    level: BatteryLevel


@dataclass(frozen=True)
class Buttons:
    y: bool = False
    x: bool = False
    b: bool = False
    a: bool = False
    sr: bool = False
    sl: bool = False
    r: bool = False
    zr: bool = False
    down: bool = False
    up: bool = False
    right: bool = False
    left: bool = False
    l: bool = False
    zl: bool = False
    minus: bool = False
    plus: bool = False
    r_stick: bool = False
    l_stick: bool = False
    home: bool = False
    capture: bool = False


class Stick(NamedTuple):
    h: int
    v: int


class Acceleration(NamedTuple):
    x: float
    y: float
    z: float


class Gyroscope(NamedTuple):
    x: float
    y: float
    z: float


@dataclass(frozen=True)
class IMUData:
    accel: Acceleration
    gyro: Gyroscope


@dataclass(frozen=True)
class JoyConStatus:
    battery: Battery
    buttons: Buttons
    stick_l: Stick
    stick_r: Stick
    imu: IMUData
