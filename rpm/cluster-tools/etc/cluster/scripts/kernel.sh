#!/bin/bash
# Modifying grub so that text mode works with iLO "textcons"
sed -i /boot/grub/grub.conf -e "s/splashimage/#splashimage/" -e "s/rhgb/vga=normal\ nomodeset/" -e "s/quiet//" -e "s/SYSFONT=[^\ ]*//"
