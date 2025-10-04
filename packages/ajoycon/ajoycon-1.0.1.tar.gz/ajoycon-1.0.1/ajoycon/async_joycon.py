"""Modern async JoyCon driver with pythonic API."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator, Callable
from contextlib import asynccontextmanager, suppress
from typing import TYPE_CHECKING

import hidraw

if TYPE_CHECKING:
    from typing import Self

from ajoycon.constants import (
    JOYCON_L_PRODUCT_ID,
    JOYCON_PRODUCT_IDS,
    JOYCON_R_PRODUCT_ID,
    JOYCON_VENDOR_ID,
)
from ajoycon.models import (
    Acceleration,
    Battery,
    BatteryLevel,
    Buttons,
    Gyroscope,
    IMUData,
    JoyConStatus,
    Stick,
)


class JoyConError(Exception):
    """Base exception for JoyCon errors."""


class JoyConConnectionError(JoyConError):
    """JoyCon connection failed."""


class AsyncJoyCon:
    """Modern async JoyCon driver with pythonic API."""

    _INPUT_REPORT_SIZE = 49
    _INPUT_REPORT_PERIOD = 0.015
    _RUMBLE_DATA = b"\x00\x01\x40\x40\x00\x01\x40\x40"

    def __init__(
        self,
        vendor_id: int,
        product_id: int,
        serial: str | None = None,
    ) -> None:
        """Initialize JoyCon connection."""
        if vendor_id != JOYCON_VENDOR_ID:
            raise ValueError(f"vendor_id is invalid: {vendor_id!r}")

        if product_id not in JOYCON_PRODUCT_IDS:
            raise ValueError(f"product_id is invalid: {product_id!r}")

        self.vendor_id = vendor_id
        self.product_id = product_id
        self.serial = serial

        # Internal state
        self._input_hooks: list[Callable[[AsyncJoyCon], None]] = []
        self._input_report = bytes(self._INPUT_REPORT_SIZE)
        self._packet_number = 0
        self._running = False
        self._update_task: asyncio.Task | None = None

        # Calibration data
        self._accel_offset_x = 0
        self._accel_offset_y = 0
        self._accel_offset_z = 0
        self._accel_coeff_x = 1.0
        self._accel_coeff_y = 1.0
        self._accel_coeff_z = 1.0

        self._gyro_offset_x = 0
        self._gyro_offset_y = 0
        self._gyro_offset_z = 0
        self._gyro_coeff_x = 1.0
        self._gyro_coeff_y = 1.0
        self._gyro_coeff_z = 1.0

        # Device colors
        self.color_body: tuple[int, int, int] = (0, 0, 0)
        self.color_btn: tuple[int, int, int] = (0, 0, 0)

        # Device handle
        self._device: hidraw.device | None = None

    async def connect(self) -> None:
        """Connect to the JoyCon device."""
        try:
            if hasattr(hidraw, "device"):  # hidapi
                self._device = hidraw.device()
                self._device.open(self.vendor_id, self.product_id, self.serial)
            elif hasattr(hidraw, "Device"):  # hid
                self._device = hidraw.Device(self.vendor_id, self.product_id, self.serial)
            else:
                raise JoyConConnectionError("Implementation of hidraw is not recognized!")
        except OSError as e:
            raise JoyConConnectionError("JoyCon connect failed") from e

        # Read device data and setup sensors
        await self._read_joycon_data()
        await self._setup_sensors()

        # Start update loop
        self._running = True
        self._update_task = asyncio.create_task(self._update_loop())

    async def disconnect(self) -> None:
        """Disconnect from the JoyCon device."""
        self._running = False
        if self._update_task:
            self._update_task.cancel()
            with suppress(asyncio.CancelledError):
                await self._update_task
            self._update_task = None

        if self._device:
            self._device.close()
            self._device = None

    async def __aenter__(self) -> Self:
        """Async context manager entry."""
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore[no-untyped-def]
        """Async context manager exit."""
        await self.disconnect()

    @property
    def is_left(self) -> bool:
        """Check if this is a left Joy-Con."""
        return self.product_id == JOYCON_L_PRODUCT_ID

    @property
    def is_right(self) -> bool:
        """Check if this is a right Joy-Con."""
        return self.product_id == JOYCON_R_PRODUCT_ID

    def _read_input_report(self) -> bytes:
        """Read input report from device."""
        if not self._device:
            raise JoyConConnectionError("Device not connected")
        return bytes(self._device.read(self._INPUT_REPORT_SIZE))

    def _write_output_report(self, command: bytes, subcommand: bytes, argument: bytes) -> None:
        """Write output report to device."""
        if not self._device:
            raise JoyConConnectionError("Device not connected")

        self._device.write(
            b"".join(
                [
                    command,
                    self._packet_number.to_bytes(1, byteorder="little"),
                    self._RUMBLE_DATA,
                    subcommand,
                    argument,
                ]
            )
        )
        self._packet_number = (self._packet_number + 1) & 0xF

    async def _send_subcmd_get_response(
        self, subcommand: bytes, argument: bytes
    ) -> tuple[bool, bytes]:
        """Send subcommand and get response."""
        self._write_output_report(b"\x01", subcommand, argument)

        # Wait for response (run in executor to avoid blocking)
        loop = asyncio.get_event_loop()
        report = await loop.run_in_executor(None, self._read_input_report)

        while report[0] != 0x21:
            report = await loop.run_in_executor(None, self._read_input_report)

        return report[13] & 0x80 != 0, report[13:]

    async def _spi_flash_read(self, address: int, size: int) -> bytes:
        """Read from SPI flash memory."""
        if size > 0x1D:
            raise ValueError("Size must be <= 0x1D")

        argument = address.to_bytes(4, "little") + size.to_bytes(1, "little")
        ack, report = await self._send_subcmd_get_response(b"\x10", argument)

        if not ack:
            raise JoyConError(f"After SPI read @ {address:#06x}: got NACK")

        if report[:2] != b"\x90\x10":
            raise JoyConError("Unexpected response to SPI read")

        return report[7 : size + 7]

    @staticmethod
    def _to_int16le_from_2bytes(hbytebe: int, lbytebe: int) -> int:
        """Convert 2 bytes to signed 16-bit little-endian integer."""
        uint16le = (lbytebe << 8) | hbytebe
        return uint16le if uint16le < 32768 else uint16le - 65536

    async def _read_joycon_data(self) -> None:
        """Read JoyCon calibration and color data."""
        color_data = await self._spi_flash_read(0x6050, 6)

        # Check for user IMU calibration data
        if await self._spi_flash_read(0x8026, 2) == b"\xB2\xA1":
            imu_cal = await self._spi_flash_read(0x8028, 24)
        else:
            # Use factory IMU calibration data
            imu_cal = await self._spi_flash_read(0x6020, 24)

        self.color_body = tuple(color_data[:3])  # type: ignore[assignment]
        self.color_btn = tuple(color_data[3:])  # type: ignore[assignment]

        # Set accelerometer calibration
        accel_offset = (
            self._to_int16le_from_2bytes(imu_cal[0], imu_cal[1]),
            self._to_int16le_from_2bytes(imu_cal[2], imu_cal[3]),
            self._to_int16le_from_2bytes(imu_cal[4], imu_cal[5]),
        )
        accel_coeff = (
            self._to_int16le_from_2bytes(imu_cal[6], imu_cal[7]),
            self._to_int16le_from_2bytes(imu_cal[8], imu_cal[9]),
            self._to_int16le_from_2bytes(imu_cal[10], imu_cal[11]),
        )
        self.set_accel_calibration(accel_offset, accel_coeff)

        # Set gyroscope calibration
        gyro_offset = (
            self._to_int16le_from_2bytes(imu_cal[12], imu_cal[13]),
            self._to_int16le_from_2bytes(imu_cal[14], imu_cal[15]),
            self._to_int16le_from_2bytes(imu_cal[16], imu_cal[17]),
        )
        gyro_coeff = (
            self._to_int16le_from_2bytes(imu_cal[18], imu_cal[19]),
            self._to_int16le_from_2bytes(imu_cal[20], imu_cal[21]),
            self._to_int16le_from_2bytes(imu_cal[22], imu_cal[23]),
        )
        self.set_gyro_calibration(gyro_offset, gyro_coeff)

    async def _setup_sensors(self) -> None:
        """Setup 6-axis sensors."""
        self._write_output_report(b"\x01", b"\x40", b"\x01")
        await asyncio.sleep(0.02)
        self._write_output_report(b"\x01", b"\x03", b"\x30")

    async def _update_loop(self) -> None:
        """Main update loop running in background."""
        loop = asyncio.get_event_loop()

        while self._running:
            try:
                # Read report in executor to avoid blocking
                report = await loop.run_in_executor(None, self._read_input_report)

                # Wait for standard input report
                while report[0] != 0x30:
                    report = await loop.run_in_executor(None, self._read_input_report)

                self._input_report = report

                # Call all registered hooks
                for callback in self._input_hooks:
                    callback(self)

            except Exception:
                # Continue on errors
                await asyncio.sleep(0.01)

    def register_update_hook(
        self, callback: Callable[[AsyncJoyCon], None]
    ) -> Callable[[AsyncJoyCon], None]:
        """Register a callback to be called on each input report update."""
        self._input_hooks.append(callback)
        return callback

    def set_gyro_calibration(
        self,
        offset_xyz: tuple[int, int, int] | None = None,
        coeff_xyz: tuple[int, int, int] | None = None,
    ) -> None:
        """Set gyroscope calibration."""
        if offset_xyz:
            self._gyro_offset_x, self._gyro_offset_y, self._gyro_offset_z = offset_xyz
        if coeff_xyz:
            cx, cy, cz = coeff_xyz
            self._gyro_coeff_x = 0x343B / cx if cx != 0x343B else 1
            self._gyro_coeff_y = 0x343B / cy if cy != 0x343B else 1
            self._gyro_coeff_z = 0x343B / cz if cz != 0x343B else 1

    def set_accel_calibration(
        self,
        offset_xyz: tuple[int, int, int] | None = None,
        coeff_xyz: tuple[int, int, int] | None = None,
    ) -> None:
        """Set accelerometer calibration."""
        if offset_xyz:
            self._accel_offset_x, self._accel_offset_y, self._accel_offset_z = offset_xyz
        if coeff_xyz:
            cx, cy, cz = coeff_xyz
            self._accel_coeff_x = 0x4000 / cx if cx != 0x4000 else 1
            self._accel_coeff_y = 0x4000 / cy if cy != 0x4000 else 1
            self._accel_coeff_z = 0x4000 / cz if cz != 0x4000 else 1

    def _get_nbit_from_input_report(self, offset_byte: int, offset_bit: int, nbit: int) -> int:
        """Get n-bit value from input report."""
        byte = self._input_report[offset_byte]
        return (byte >> offset_bit) & ((1 << nbit) - 1)

    # Battery properties
    @property
    def battery_charging(self) -> bool:
        """Get battery charging status."""
        return bool(self._get_nbit_from_input_report(2, 4, 1))

    @property
    def battery_level(self) -> BatteryLevel:
        """Get battery level."""
        return BatteryLevel(self._get_nbit_from_input_report(2, 5, 3))

    @property
    def battery(self) -> Battery:
        """Get battery status."""
        return Battery(charging=self.battery_charging, level=self.battery_level)

    # Button properties
    @property
    def button_y(self) -> bool:
        return bool(self._get_nbit_from_input_report(3, 0, 1))

    @property
    def button_x(self) -> bool:
        return bool(self._get_nbit_from_input_report(3, 1, 1))

    @property
    def button_b(self) -> bool:
        return bool(self._get_nbit_from_input_report(3, 2, 1))

    @property
    def button_a(self) -> bool:
        return bool(self._get_nbit_from_input_report(3, 3, 1))

    @property
    def button_right_sr(self) -> bool:
        return bool(self._get_nbit_from_input_report(3, 4, 1))

    @property
    def button_right_sl(self) -> bool:
        return bool(self._get_nbit_from_input_report(3, 5, 1))

    @property
    def button_r(self) -> bool:
        return bool(self._get_nbit_from_input_report(3, 6, 1))

    @property
    def button_zr(self) -> bool:
        return bool(self._get_nbit_from_input_report(3, 7, 1))

    @property
    def button_minus(self) -> bool:
        return bool(self._get_nbit_from_input_report(4, 0, 1))

    @property
    def button_plus(self) -> bool:
        return bool(self._get_nbit_from_input_report(4, 1, 1))

    @property
    def button_r_stick(self) -> bool:
        return bool(self._get_nbit_from_input_report(4, 2, 1))

    @property
    def button_l_stick(self) -> bool:
        return bool(self._get_nbit_from_input_report(4, 3, 1))

    @property
    def button_home(self) -> bool:
        return bool(self._get_nbit_from_input_report(4, 4, 1))

    @property
    def button_capture(self) -> bool:
        return bool(self._get_nbit_from_input_report(4, 5, 1))

    @property
    def button_charging_grip(self) -> bool:
        return bool(self._get_nbit_from_input_report(4, 7, 1))

    @property
    def button_down(self) -> bool:
        return bool(self._get_nbit_from_input_report(5, 0, 1))

    @property
    def button_up(self) -> bool:
        return bool(self._get_nbit_from_input_report(5, 1, 1))

    @property
    def button_right(self) -> bool:
        return bool(self._get_nbit_from_input_report(5, 2, 1))

    @property
    def button_left(self) -> bool:
        return bool(self._get_nbit_from_input_report(5, 3, 1))

    @property
    def button_left_sr(self) -> bool:
        return bool(self._get_nbit_from_input_report(5, 4, 1))

    @property
    def button_left_sl(self) -> bool:
        return bool(self._get_nbit_from_input_report(5, 5, 1))

    @property
    def button_l(self) -> bool:
        return bool(self._get_nbit_from_input_report(5, 6, 1))

    @property
    def button_zl(self) -> bool:
        return bool(self._get_nbit_from_input_report(5, 7, 1))

    @property
    def buttons(self) -> Buttons:
        return Buttons(
            y=self.button_y,
            x=self.button_x,
            b=self.button_b,
            a=self.button_a,
            sr=self.button_right_sr,
            sl=self.button_right_sl,
            r=self.button_r,
            zr=self.button_zr,
            down=self.button_down,
            up=self.button_up,
            right=self.button_right,
            left=self.button_left,
            l=self.button_l,
            zl=self.button_zl,
            minus=self.button_minus,
            plus=self.button_plus,
            r_stick=self.button_r_stick,
            l_stick=self.button_l_stick,
            home=self.button_home,
            capture=self.button_capture,
        )

    # Analog stick properties
    @property
    def stick_left_horizontal(self) -> int:
        return self._get_nbit_from_input_report(6, 0, 8) | (
            self._get_nbit_from_input_report(7, 0, 4) << 8
        )

    @property
    def stick_left_vertical(self) -> int:
        return self._get_nbit_from_input_report(7, 4, 4) | (
            self._get_nbit_from_input_report(8, 0, 8) << 4
        )

    @property
    def stick_right_horizontal(self) -> int:
        return self._get_nbit_from_input_report(9, 0, 8) | (
            self._get_nbit_from_input_report(10, 0, 4) << 8
        )

    @property
    def stick_right_vertical(self) -> int:
        return self._get_nbit_from_input_report(10, 4, 4) | (
            self._get_nbit_from_input_report(11, 0, 8) << 4
        )

    @property
    def stick_l(self) -> Stick:
        return Stick(self.stick_left_horizontal, self.stick_left_vertical)

    @property
    def stick_r(self) -> Stick:
        return Stick(self.stick_right_horizontal, self.stick_right_vertical)

    # IMU properties
    def get_accel_x(self, sample_idx: int = 0) -> float:
        """Get accelerometer X value (calibrated)."""
        if sample_idx not in (0, 1, 2):
            raise IndexError("sample_idx should be between 0 and 2")
        data = self._to_int16le_from_2bytes(
            self._input_report[13 + sample_idx * 12],
            self._input_report[14 + sample_idx * 12],
        )
        return (data - self._accel_offset_x) * self._accel_coeff_x

    def get_accel_y(self, sample_idx: int = 0) -> float:
        """Get accelerometer Y value (calibrated)."""
        if sample_idx not in (0, 1, 2):
            raise IndexError("sample_idx should be between 0 and 2")
        data = self._to_int16le_from_2bytes(
            self._input_report[15 + sample_idx * 12],
            self._input_report[16 + sample_idx * 12],
        )
        return (data - self._accel_offset_y) * self._accel_coeff_y

    def get_accel_z(self, sample_idx: int = 0) -> float:
        """Get accelerometer Z value (calibrated)."""
        if sample_idx not in (0, 1, 2):
            raise IndexError("sample_idx should be between 0 and 2")
        data = self._to_int16le_from_2bytes(
            self._input_report[17 + sample_idx * 12],
            self._input_report[18 + sample_idx * 12],
        )
        return (data - self._accel_offset_z) * self._accel_coeff_z

    def get_gyro_x(self, sample_idx: int = 0) -> float:
        """Get gyroscope X value (calibrated)."""
        if sample_idx not in (0, 1, 2):
            raise IndexError("sample_idx should be between 0 and 2")
        data = self._to_int16le_from_2bytes(
            self._input_report[19 + sample_idx * 12],
            self._input_report[20 + sample_idx * 12],
        )
        return (data - self._gyro_offset_x) * self._gyro_coeff_x

    def get_gyro_y(self, sample_idx: int = 0) -> float:
        """Get gyroscope Y value (calibrated)."""
        if sample_idx not in (0, 1, 2):
            raise IndexError("sample_idx should be between 0 and 2")
        data = self._to_int16le_from_2bytes(
            self._input_report[21 + sample_idx * 12],
            self._input_report[22 + sample_idx * 12],
        )
        return (data - self._gyro_offset_y) * self._gyro_coeff_y

    def get_gyro_z(self, sample_idx: int = 0) -> float:
        """Get gyroscope Z value (calibrated)."""
        if sample_idx not in (0, 1, 2):
            raise IndexError("sample_idx should be between 0 and 2")
        data = self._to_int16le_from_2bytes(
            self._input_report[23 + sample_idx * 12],
            self._input_report[24 + sample_idx * 12],
        )
        return (data - self._gyro_offset_z) * self._gyro_coeff_z

    @property
    def acceleration(self) -> Acceleration:
        """Get acceleration in g-forces."""
        c = 4.0 / 0x4000
        return Acceleration(
            x=self.get_accel_x() * c,
            y=self.get_accel_y() * c,
            z=self.get_accel_z() * c,
        )

    @property
    def gyroscope(self) -> Gyroscope:
        """Get gyroscope in degrees per second."""
        c = 0.06103
        return Gyroscope(
            x=self.get_gyro_x() * c,
            y=self.get_gyro_y() * c,
            z=self.get_gyro_z() * c,
        )

    @property
    def imu(self) -> IMUData:
        """Get IMU data (accelerometer + gyroscope)."""
        return IMUData(accel=self.acceleration, gyro=self.gyroscope)

    @property
    def status(self) -> JoyConStatus:
        return JoyConStatus(
            battery=self.battery,
            buttons=self.buttons,
            stick_l=self.stick_l,
            stick_r=self.stick_r,
            imu=self.imu,
        )

    # Control methods
    async def set_player_lamp(self, pattern: int) -> None:
        """Set player lamp pattern."""
        self._write_output_report(b"\x01", b"\x30", pattern.to_bytes(1, byteorder="little"))

    async def set_player_lamp_on(self, on_pattern: int) -> None:
        """Set player lamp on pattern."""
        self._write_output_report(
            b"\x01", b"\x30", (on_pattern & 0xF).to_bytes(1, byteorder="little")
        )

    async def set_player_lamp_flashing(self, flashing_pattern: int) -> None:
        """Set player lamp flashing pattern."""
        self._write_output_report(
            b"\x01", b"\x30", ((flashing_pattern & 0xF) << 4).to_bytes(1, byteorder="little")
        )


@asynccontextmanager
async def connect_joycon(
    vendor_id: int,
    product_id: int,
    serial: str | None = None,
) -> AsyncIterator[AsyncJoyCon]:
    """Context manager for connecting to a JoyCon."""
    joycon = AsyncJoyCon(vendor_id, product_id, serial)
    await joycon.connect()
    try:
        yield joycon
    finally:
        await joycon.disconnect()
