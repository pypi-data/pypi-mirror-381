"""Basic async JoyCon usage example."""

import asyncio

from ajoycon import discover_joycons


async def main() -> None:
    joycons = discover_joycons()
    if not joycons:
        print("No JoyCon found!")
        return

    device = joycons[0]
    print(f"Connecting to {device.type.value.upper()} JoyCon...")

    async with device.connect() as joycon:
        print(f"Connected!")

        for i in range(50):
            status = joycon.status

            print(f"\n--- Update {i+1} ---")
            print(f"Battery: {status.battery.level.name}")
            print(f"Charging: {status.battery.charging}")

            pressed = []
            if status.buttons.a:
                pressed.append("A")
            if status.buttons.b:
                pressed.append("B")
            if status.buttons.home:
                pressed.append("HOME")

            if pressed:
                print(f"Buttons: {', '.join(pressed)}")

            print(f"Stick L: {status.stick_l}")
            print(f"Stick R: {status.stick_r}")
            print(f"Accel: {status.imu.accel}")
            print(f"Gyro: {status.imu.gyro}")

            await asyncio.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(main())
