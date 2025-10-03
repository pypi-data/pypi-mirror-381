"""Async button event tracking for JoyCon controllers."""

import asyncio
from collections import deque
from collections.abc import AsyncIterator
from dataclasses import dataclass
from enum import Enum
from typing import Any

from ajoycon.async_joycon import AsyncJoyCon


class ButtonEvent(Enum):
    """Button event types."""

    # Right JoyCon buttons
    Y = "y"
    X = "x"
    B = "b"
    A = "a"
    R = "r"
    ZR = "zr"
    RIGHT_SR = "right_sr"
    RIGHT_SL = "right_sl"

    # Left JoyCon buttons
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    L = "l"
    ZL = "zl"
    LEFT_SR = "left_sr"
    LEFT_SL = "left_sl"

    # Shared buttons
    PLUS = "plus"
    MINUS = "minus"
    HOME = "home"
    CAPTURE = "capture"
    STICK_L = "stick_l"
    STICK_R = "stick_r"


@dataclass(frozen=True)
class JoyConButtonEvent:
    """Button state change event."""

    button: ButtonEvent
    pressed: bool

    @property
    def released(self) -> bool:
        """Check if button was released."""
        return not self.pressed


class ButtonEventJoyCon(AsyncJoyCon):
    """JoyCon with button event tracking."""

    def __init__(
        self,
        vendor_id: int,
        product_id: int,
        serial: str | None = None,
        *,
        track_sticks: bool = False,
    ) -> None:
        """
        Initialize button event JoyCon.

        Args:
            vendor_id: Vendor ID
            product_id: Product ID
            serial: Serial number
            track_sticks: Track analog stick button presses
        """
        super().__init__(vendor_id, product_id, serial)

        self._track_sticks = track_sticks
        self._event_queue: deque[JoyConButtonEvent] = deque()

        # Previous button states
        self._prev: dict[str, Any] = {
            # Right buttons
            "y": False,
            "x": False,
            "b": False,
            "a": False,
            "r": False,
            "zr": False,
            "right_sr": False,
            "right_sl": False,
            # Left buttons
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "l": False,
            "zl": False,
            "left_sr": False,
            "left_sl": False,
            # Shared buttons
            "plus": False,
            "minus": False,
            "home": False,
            "capture": False,
            "stick_l": False,
            "stick_r": False,
        }

        # Register appropriate update hook based on controller type
        if self.is_left:
            self.register_update_hook(self._event_tracking_update_hook_left)
        else:
            self.register_update_hook(self._event_tracking_update_hook_right)

    def _check_button(self, name: str, event: ButtonEvent, current: bool) -> None:
        """Check if button state changed and emit event."""
        if self._prev[name] != current:
            self._prev[name] = current
            self._event_queue.append(JoyConButtonEvent(button=event, pressed=current))

    def _event_tracking_update_hook_right(self, joycon: AsyncJoyCon) -> None:
        """Update hook for right JoyCon buttons."""
        if self._track_sticks:
            self._check_button("stick_r", ButtonEvent.STICK_R, self.button_r_stick)

        self._check_button("r", ButtonEvent.R, self.button_r)
        self._check_button("zr", ButtonEvent.ZR, self.button_zr)
        self._check_button("plus", ButtonEvent.PLUS, self.button_plus)
        self._check_button("a", ButtonEvent.A, self.button_a)
        self._check_button("b", ButtonEvent.B, self.button_b)
        self._check_button("x", ButtonEvent.X, self.button_x)
        self._check_button("y", ButtonEvent.Y, self.button_y)
        self._check_button("home", ButtonEvent.HOME, self.button_home)
        self._check_button("right_sr", ButtonEvent.RIGHT_SR, self.button_right_sr)
        self._check_button("right_sl", ButtonEvent.RIGHT_SL, self.button_right_sl)

    def _event_tracking_update_hook_left(self, joycon: AsyncJoyCon) -> None:
        """Update hook for left JoyCon buttons."""
        if self._track_sticks:
            self._check_button("stick_l", ButtonEvent.STICK_L, self.button_l_stick)

        self._check_button("l", ButtonEvent.L, self.button_l)
        self._check_button("zl", ButtonEvent.ZL, self.button_zl)
        self._check_button("minus", ButtonEvent.MINUS, self.button_minus)
        self._check_button("up", ButtonEvent.UP, self.button_up)
        self._check_button("down", ButtonEvent.DOWN, self.button_down)
        self._check_button("left", ButtonEvent.LEFT, self.button_left)
        self._check_button("right", ButtonEvent.RIGHT, self.button_right)
        self._check_button("capture", ButtonEvent.CAPTURE, self.button_capture)
        self._check_button("left_sr", ButtonEvent.LEFT_SR, self.button_left_sr)
        self._check_button("left_sl", ButtonEvent.LEFT_SL, self.button_left_sl)

    def poll_events(self) -> list[JoyConButtonEvent]:
        """
        Poll all pending button events.

        Returns:
            List of button events since last poll.
        """
        events = list(self._event_queue)
        self._event_queue.clear()
        return events

    async def wait_for_event(self, timeout: float | None = None) -> JoyConButtonEvent | None:
        """
        Wait for next button event.

        Args:
            timeout: Maximum time to wait in seconds (None for no timeout)

        Returns:
            Next button event, or None if timeout
        """
        start_time = asyncio.get_event_loop().time()

        while True:
            if self._event_queue:
                return self._event_queue.popleft()

            if timeout is not None:
                elapsed = asyncio.get_event_loop().time() - start_time
                if elapsed >= timeout:
                    return None

            await asyncio.sleep(0.001)

    async def event_stream(self) -> AsyncIterator[JoyConButtonEvent]:
        """
        Async iterator that yields button events as they occur.

        Example:
            async for event in joycon.event_stream():
                print(f"{event.button.value}: {'pressed' if event.pressed else 'released'}")
        """
        while self._running:
            event = await self.wait_for_event(timeout=0.1)
            if event:
                yield event
