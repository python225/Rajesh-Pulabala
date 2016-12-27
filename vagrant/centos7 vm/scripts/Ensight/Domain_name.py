#!/usr/bin/python

import json
import subprocess

#1) for getting DNS Domain Name 
def get_dna():
    name = subprocess.check_output("hostname | cut -d'.' -f1", shell=True)
    return name
var1 = get_dna()


all = {"DomainName":var1}

print json.dumps(all)