"""Device discovery for JoyCon controllers."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

import hid

if TYPE_CHECKING:
    from ajoycon.async_joycon import AsyncJoyCon

from ajoycon.constants import JOYCON_L_PRODUCT_ID, JOYCON_PRODUCT_IDS, JOYCON_VENDOR_ID


class JoyConType(Enum):
    LEFT = "left"
    RIGHT = "right"


@dataclass(frozen=True)
class JoyConDevice:
    vendor_id: int
    product_id: int
    serial: str | None
    type: JoyConType

    def connect(self) -> AsyncJoyCon:
        from ajoycon.async_joycon import connect_joycon

        return connect_joycon(self.vendor_id, self.product_id, self.serial)


def discover_joycons() -> list[JoyConDevice]:
    devices = hid.enumerate(0, 0)
    joycons: list[JoyConDevice] = []

    for device in devices:
        vendor_id = device["vendor_id"]
        product_id = device["product_id"]
        serial = device.get("serial") or device.get("serial_number")

        if vendor_id != JOYCON_VENDOR_ID or product_id not in JOYCON_PRODUCT_IDS:
            continue

        joy_type = JoyConType.LEFT if product_id == JOYCON_L_PRODUCT_ID else JoyConType.RIGHT
        joycons.append(JoyConDevice(vendor_id, product_id, serial, joy_type))

    return joycons
