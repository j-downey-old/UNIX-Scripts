#!/bin/bash
args=("$@")
brightness=`sudo cat /sys/class/backlight/intel_backlight/brightness`
mod=${args[0]}
echo `echo $((brightness+mod)) | sudo tee /sys/class/backlight/intel_backlight/brightness`
