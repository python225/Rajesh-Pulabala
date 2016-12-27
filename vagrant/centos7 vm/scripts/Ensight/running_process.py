#!/usr/bin/python
import psutil
import json
import psutil
import os
import platform

#processes_name = psutil.get_process_list()
#print processes_name

def getprocess():

        for proc in psutil.process_iter():
            try:
               pinfo = proc.as_dict(attrs=['pid', 'name'])
            except psutil.NoSuchProcess:
               pass
            else:
               print(pinfo)
processes_id_name = getprocess()


#output = {

 #      'processes_id_name':{
  #        'process_list' :processes_name,
   #     },
#}
print json.dumps(processes_id_name, indent=4)
