#!/bin/bash

id=`xinput | grep "Touchpad" | grep -oE "id=[0123456789]+" | grep -oE "[0123456789]+"` 
state=`xinput list-props "$id" | grep "Device Enabled" | grep -o "[01]$"`

if [ $state == '1' ];then
  xinput --disable $id
else
  xinput --enable $id
fi
