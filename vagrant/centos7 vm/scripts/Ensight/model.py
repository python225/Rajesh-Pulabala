#!/usr/bin/python

import json
import subprocess



def get_mod():
       model = subprocess.check_output("dmidecode | grep UUID",shell=True)
       return model
var3 = get_mod()

all = {'Model':var3}

print json.dumps(all)