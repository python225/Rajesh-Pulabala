#!/usr/bin/python

import platform
import json
import os


Description = platform.platform()
Machine = platform.machine()
Processor = platform.processor()
SystemOS = platform.system()
Release = platform.release()
Version = platform.version()
x = platform.linux_distribution()
y = x[0]


full = {'OperatingSystem': [{'Description':Description, 'ProductName':y, 'Machine':Machine, 'Processor':Processor, 'System OS':SystemOS, 'Release':Release, 'Version':Version}]}

print json.dumps(full, indent=4)
                                 
