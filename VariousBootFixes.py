#!/bin/python3

import re
import os

with open ("/usr/share/plymouth/themes/default.grub", 'r') as plymouth_file:
  text = plymouth_file.read()
  text = re.sub("background_color[^;]*;", "background_color 35,00,60 ;", text)
with open ("/usr/share/plymouth/themes/default.grub", 'w') as new_plymouth_file:
  new_plymouth_file.write(text)
  
os.chdir("/boot/grub")
for file in os.listdir("/media/Manjaro/boot"):
  if file.startswith("initramfs") and not file.endswith("fallback.img"):
    ramdisk = file
with open ("grub.cfg") as grub_cfg:
  text = grub_cfg.read()
text = re.sub("initrd /boot/intel-ucode.img[^}]*}",
              "initrd /boot/intel-ucode.img\n\tinitrd /boot/" + ramdisk + "\n}",
              text)
with open ("grub.cfg", "w") as grub_cfg:
  grub_cfg.write(text)
