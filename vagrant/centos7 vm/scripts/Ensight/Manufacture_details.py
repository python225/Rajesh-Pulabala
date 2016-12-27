#!/usr/bin/python

import json
import subprocess

# 1)For getting manufacture details of the current running system

def get_mani():
      manuf = subprocess.check_output("dmidecode | grep Manufacturer | sed -n '1p'| awk '{print$2,$3}'", shell=True)
      return manuf
var2 = get_mani()
all = {'Manfacture':var2}
print json.dumps(all)
