# ajoycon

Modern async Python driver for Nintendo Switch Joy-Con controllers

Fork of [tokoroten-lab/joycon-python](https://github.com/tokoroten-lab/joycon-python)

## Install

```shell
pip install ajoycon
```

### Linux Setup

```shell
sudo curl -o /etc/udev/rules.d/50-nintendo-switch.rules https://raw.githubusercontent.com/DanielOgorchock/linux/refs/heads/master/drivers/hid/50-nintendo-switch.rules
sudo udevadm control --reload-rules && sudo udevadm trigger
```

Reconnect your JoyCon.

## Usage

```python
import asyncio
from ajoycon import discover_joycons

async def main():
    joycons = discover_joycons()
    if not joycons:
        return

    async with joycons[0].connect() as joycon:
        status = joycon.status
        print(f"Battery: {status.battery.level.name}")
        print(f"Buttons: {status.buttons}")
        print(f"Sticks: {status.stick_l}, {status.stick_r}")
        print(f"IMU: {status.imu}")

asyncio.run(main())
```

## Requirements

- Python 3.13+
- hidapi
- pyglm

## License

MIT
