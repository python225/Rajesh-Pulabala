#!/usr/bin/python

import json
import psutil

def get_proc1():
       totl = psutil.cpu_count()
       return totl
var4 = get_proc1()
all = {"NumberOfLogicalProcessors":var4}
print json.dumps(all)