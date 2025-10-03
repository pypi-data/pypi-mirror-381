"""Async gyroscope tracking for JoyCon controllers."""

import asyncio
import time
from typing import NamedTuple

from glm import angleAxis, eulerAngles, quat, vec2, vec3

from ajoycon.async_joycon import AsyncJoyCon


class Rotation(NamedTuple):
    """Rotation in Euler angles (radians)."""

    x: float
    y: float
    z: float


class GyroTrackingJoyCon(AsyncJoyCon):
    """JoyCon with gyroscope orientation tracking."""

    def __init__(
        self,
        vendor_id: int,
        product_id: int,
        serial: str | None = None,
        *,
        invert_left_ime_yz: bool = True,
    ) -> None:
        """
        Initialize gyro tracking JoyCon.

        Args:
            vendor_id: Vendor ID
            product_id: Product ID
            serial: Serial number
            invert_left_ime_yz: Invert Y/Z axis for left JoyCon to match right
        """
        super().__init__(vendor_id, product_id, serial)

        # IMU coefficient for left JoyCon inversion
        self._ime_yz_coeff = -1 if invert_left_ime_yz and self.is_left else 1

        # Orientation tracking state
        self.direction_X = vec3(1, 0, 0)
        self.direction_Y = vec3(0, 1, 0)
        self.direction_Z = vec3(0, 0, 1)
        self.direction_Q = quat()

        # Calibration state
        self._is_calibrating = False
        self._calibration_end_time = 0.0
        self._calibration_accumulator = vec3(0)
        self._calibration_count = 0

        # Register update hook
        self.register_update_hook(self._gyro_update_hook)

    @property
    def pointer(self) -> vec2 | None:
        """Get pointer position (for pointing at screen)."""
        d = self.direction
        if d.x <= 0:
            return None
        return vec2(d.y, -d.z) / d.x

    @property
    def direction(self) -> vec3:
        """Get current direction vector."""
        return self.direction_X

    @property
    def rotation(self) -> Rotation:
        """Get current rotation in Euler angles."""
        euler = -eulerAngles(self.direction_Q)
        return Rotation(x=euler.x, y=euler.y, z=euler.z)

    async def calibrate(self, seconds: float = 2.0) -> None:
        """
        Calibrate gyroscope by measuring drift while stationary.

        Args:
            seconds: Duration to calibrate for (default 2 seconds)
        """
        self._calibration_accumulator = vec3(0)
        self._calibration_count = 0
        self._is_calibrating = True
        self._calibration_end_time = time.time() + seconds

        # Wait for calibration to complete
        await asyncio.sleep(seconds)

    def _set_calibration(self, gyro_offset: tuple[float, float, float] | None = None) -> None:
        """Set gyroscope calibration offset."""
        if not gyro_offset:
            c = vec3(1, self._ime_yz_coeff, self._ime_yz_coeff)
            offset = self._calibration_accumulator * c
            offset /= self._calibration_count
            gyro_offset = (
                offset.x + self._gyro_offset_x,
                offset.y + self._gyro_offset_y,
                offset.z + self._gyro_offset_z,
            )

        self._is_calibrating = False
        self.set_gyro_calibration(gyro_offset)

    def reset_orientation(self) -> None:
        """Reset orientation to default (identity)."""
        self.direction_X = vec3(1, 0, 0)
        self.direction_Y = vec3(0, 1, 0)
        self.direction_Z = vec3(0, 0, 1)
        self.direction_Q = quat()

    def _gyro_update_hook(self, joycon: AsyncJoyCon) -> None:
        """Update hook called on each input report."""
        # Handle calibration
        if self._is_calibrating:
            if time.time() >= self._calibration_end_time:
                self._set_calibration()
            else:
                # Accumulate gyro samples for calibration
                for i in range(3):
                    gx = self.get_gyro_x(i)
                    gy = self.get_gyro_y(i) * self._ime_yz_coeff
                    gz = self.get_gyro_z(i) * self._ime_yz_coeff
                    self._calibration_accumulator += vec3(gx, gy, gz)
                self._calibration_count += 3
            return

        # Update orientation from gyroscope
        c = 0.0001694 * 3.1415926536  # Convert to radians
        c2 = c * self._ime_yz_coeff

        for i in range(3):
            gx = self.get_gyro_x(i) * c
            gy = self.get_gyro_y(i) * c2
            gz = self.get_gyro_z(i) * c2

            # Apply rotation using quaternions
            # TODO: find out why 1/86 works instead of proper time step
            rotation = (
                angleAxis(gx * (-1 / 86), self.direction_X)
                * angleAxis(gy * (-1 / 86), self.direction_Y)
                * angleAxis(gz * (-1 / 86), self.direction_Z)
            )

            self.direction_X *= rotation
            self.direction_Y *= rotation
            self.direction_Z *= rotation
            self.direction_Q *= rotation
