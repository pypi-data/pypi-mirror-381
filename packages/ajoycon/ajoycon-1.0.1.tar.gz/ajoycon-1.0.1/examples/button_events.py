"""Button event tracking example."""

import asyncio

from ajoycon import ButtonEventJoyCon, JoyConType, discover_joycons


async def main() -> None:
    """Track button press/release events."""
    joycons = discover_joycons()
    device = next((jc for jc in joycons if jc.type == JoyConType.RIGHT), None)

    if not device:
        print("No right JoyCon found!")
        return

    print("Connecting to JoyCon...")
    print("Press buttons to see events. Press HOME to exit.\n")

    joycon = ButtonEventJoyCon(device.vendor_id, device.product_id, device.serial)
    await joycon.connect()

    try:
        # Method 1: Async iterator
        async for event in joycon.event_stream():
            action = "pressed" if event.pressed else "released"
            print(f"{event.button.value.upper():12s} {action}")

            # Exit on HOME button press
            if event.button.value == "home" and event.pressed:
                break

    finally:
        await joycon.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
