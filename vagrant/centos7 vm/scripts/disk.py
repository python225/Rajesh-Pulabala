from __future__ import division
import subprocess
import datetime
import json
import socket
import fcntl
import struct
import psutil
import time
import datetime

def get_cp():
	a = psutil.cpu_percent()
	return (a)

list = []

for i in range(1,6):
    time.sleep(5)
    list.append(get_cp())
all = list
print all 
