#!/usr/bin/python

import json
import subprocess

#1) for getting DNS Host Name 
def get_dom():
    nam = subprocess.check_output("hostname | cut -d'.' -f2", shell=True)
    return nam
va1 = get_dom()

all = {"DNSHostName":var1}

print json.dumps(all)



