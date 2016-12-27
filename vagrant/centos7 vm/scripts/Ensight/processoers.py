#!/usr/bin/python

import psutil
import json

total = psutil.cpu_count() 
physical = psutil.cpu_count(logical=False)


result = {'Processor_Info':    {'NumberOfLogicalProcessors':total, 'NumberOfProcessors':physical}}


print json.dumps(result, indent=2)

