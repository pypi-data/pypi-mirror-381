"""Gyroscope orientation tracking example."""

import asyncio

from ajoycon import GyroTrackingJoyCon, find_first_right_joycon


async def main() -> None:
    """Track JoyCon orientation using gyroscope."""
    device = find_first_right_joycon()
    if not device:
        print("No right JoyCon found!")
        return

    print("Connecting to JoyCon...")
    joycon = GyroTrackingJoyCon(device.vendor_id, device.product_id, device.serial)
    await joycon.connect()

    try:
        print("Calibrating... (keep controller still)")
        await joycon.calibrate(seconds=2.0)
        print("Calibration complete!\n")

        print("Move the controller around. Press Ctrl+C to exit.\n")

        while True:
            # Get rotation in Euler angles
            rotation = joycon.rotation
            print(f"Rotation: X={rotation.x:6.2f}, Y={rotation.y:6.2f}, Z={rotation.z:6.2f}", end="\r")

            # Get direction vector
            direction = joycon.direction
            # print(f"Direction: ({direction.x:.2f}, {direction.y:.2f}, {direction.z:.2f})")

            # Get pointer position (for pointing at screen)
            pointer = joycon.pointer
            if pointer:
                # Convert to screen coordinates (example for 1920x1080)
                screen_x = int((pointer.x + 1) * 960)
                screen_y = int((pointer.y + 1) * 540)
                # print(f"Pointer: ({screen_x}, {screen_y})")

            await asyncio.sleep(0.05)

    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        await joycon.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
