#!/bin/bash
echo  'SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="7523", MODE:="0777", GROUP:="dialout", SYMLINK+="arduino_nano"' >/etc/udev/rules.d/arduino.rules

sudo adduser $USER dialout

service udev reload
sleep 2
service udev restart