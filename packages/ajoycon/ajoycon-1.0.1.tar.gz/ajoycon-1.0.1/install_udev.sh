#!/bin/bash
set -e

echo "Installing udev rules for Nintendo Switch Joy-Con controllers..."

# Copy udev rules
sudo cp 50-nintendo-switch.rules /etc/udev/rules.d/

# Reload udev rules
sudo udevadm control --reload-rules
sudo udevadm trigger

echo "Done! Please disconnect and reconnect your Joy-Cons."
echo ""
echo "Note: The kernel hid_nintendo driver conflicts with hidapi access."
echo "If Joy-Cons are still not detected, blacklist it by running:"
echo "  echo 'blacklist hid_nintendo' | sudo tee /etc/modprobe.d/blacklist-nintendo.conf"
echo "  sudo rmmod hid_nintendo"
echo "Then reconnect your Joy-Cons."
