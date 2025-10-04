# ajoycon

Modern async Python driver for Nintendo Switch Joy-Con controllers

Fork of [tokoroten-lab/joycon-python](https://github.com/tokoroten-lab/joycon-python)

## Install

### Using uv (recommended)

```shell
uv add ajoycon
```

### Using pip

```shell
pip install ajoycon
```

### Linux Setup

#### 1. Install system dependencies

```shell
sudo apt install libhidapi-dev libudev-dev
```

#### 2. Install hidapi with hidraw backend support

The default hidapi package doesn't support Bluetooth HID devices properly. Install from source:

**Using uv:**
```shell
uv remove hidapi
uv add hidapi --no-binary hidapi
```

**Using pip:**
```shell
pip uninstall hidapi
pip install hidapi --no-binary hidapi
```

#### 3. Setup udev rules

Use the provided installation script:

```shell
./install_udev.sh
```

Or manually:

```shell
sudo cp 50-nintendo-switch.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger
```

#### 4. Blacklist the kernel hid_nintendo driver

The kernel driver conflicts with hidapi access:

```shell
echo "blacklist hid_nintendo" | sudo tee /etc/modprobe.d/blacklist-nintendo.conf
sudo rmmod hid_nintendo  # Unload the module (or reboot)
```

#### 5. Connect your Joy-Cons

Pair and connect your Joy-Cons via Bluetooth, then reconnect them after completing the setup above.

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
- hidapi (built with hidraw backend for Linux Bluetooth support)
- pyglm

### System Dependencies (Linux)

- libhidapi-dev
- libudev-dev

## License

MIT
