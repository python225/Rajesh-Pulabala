#!/usr/bin/python

import json
import psutil

def get_proc2():
       physical = psutil.cpu_count(logical=False)
       return physical
var5 = get_proc2()
all = {"NumberOfProcessors":var5}
print json.dumps(all)