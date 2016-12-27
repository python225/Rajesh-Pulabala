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


def get_readbytes_with_timestamp():
        ts_return_list = []
        ts_a = psutil.cpu_percent() 
        ts_time_stamp = time.time()
        ts_st = datetime.datetime.fromtimestamp(ts_time_stamp).strftime('%Y-%m-%d %H:%M:%S')
        ts_return_list.append(ts_st)
        ts_return_list.append((ts_a))
        return ts_return_list
def get_readbytes(): 
        a = psutil.cpu_percent() 
        d = (a)
        return float(d)
        
disk_stats = []
disk_stats_with_timestamp = []
for i in range(1,6):
   time.sleep(5)
   
   disk_stats.append(get_readbytes())
   disk_stats_with_timestamp.append(get_readbytes_with_timestamp()) 


x = float(sum(disk_stats) /(len(disk_stats)))
y = max(disk_stats)
z = min(disk_stats)
RecordCount = len(disk_stats)
aa = "Logical Volume Manager" 
bb = "Total"
cc = "avg_disk_writebytes_write"
dd = "Avg.Disk Bytes/write"
ee = "20sec"


all = {'Duration: ':ee,'PerformanceCounterCategory: ':aa,'PerformanceCounterInstanceName: ':bb,'PerformanceCounterLabel: ':cc,'PerformanceCounterName: ':dd,'AverageValue: ':x,'MaxValue: ':y,'MinValue: ':z,'RecordCount: ':RecordCount}
#for k,v in sorted(all.items()):
#	print k, v
print json.dumps(all, indent=4)
value = {'Values':disk_stats_with_timestamp}
	
print json.dumps(value, indent=4)
