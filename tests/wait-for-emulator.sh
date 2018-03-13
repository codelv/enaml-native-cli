#!/bin/bash

# Originally written by Ralf Kistner <ralf@embarkmobile.com>, but placed in the public domain
# Edited for log brevity by Affian <https://github.com/viperwarp>

set +e

bootanim=""
failcounter=0
echo "Waiting for Emulator"
until [[ "$bootanim" =~ "stopped" ]]; do
   bootanim=`adb -e shell getprop init.svc.bootanim 2>&1`
   echo -ne "."
   if [[ "$bootanim" =~ "not found" ]]; then
      let "failcounter += 1"
      if [[ $failcounter -gt 15 ]]; then
        echo "Failed to start emulator"
        exit 1
      fi
   fi
   sleep 2
done
echo "Done"