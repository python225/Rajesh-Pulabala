#!/usr/bin/python

import netifaces
import json
import socket
import fcntl
import struct
import psutil
import logging
import os
import platform
import dmidecode
import subprocess
import datetime
from subprocess import check_output
# getting active connection on my localhost



def get_tm():
       a = datetime.datetime.now()
       return str(a)
var100 = get_tm()

def get_dom():
    nam = subprocess.check_output("hostname | cut -d'.' -f2", shell=True)
    return nam
va1 = get_dom()

def get_active_connections():
  active_connections= []
  for connection in psutil.net_connections():
    tmp_active_connection = {}
    if connection.type == 1:
      tmp_active_connection['Connection_Type'] = 'TCP'
      tmp_active_connection['Local_Port'] = connection.laddr[1]
      tmp_active_connection['LocalIP'] = connection.laddr[0]
      tmp_active_connection['ReportDateTime'] = var100
      tmp_active_connection['LocalHostName'] = va1
      if not connection.raddr:
        tmp_active_connection['RemoteIP'] = 'Null'
        tmp_active_connection['Remote-Port'] = 'Null'
      else:
        tmp_active_connection['RemoteIP'] = connection.raddr[0]
        tmp_active_connection['Remote_Port'] = connection.raddr[1]
        cmd_nslook = 'nslookup ' + connection.raddr[0] + '| grep name | cut -d' ' -f3'
        remote_hostname = subprocess.call("cmd_nslook", shell=True)
        tmp_active_connection['RemoteHostName'] = remote_hostname

    elif connection.type  == 2:
      tmp_active_connection['Connection_Type'] = 'UDP'
      tmp_active_connection['Local_Port'] = connection.laddr[1]
      tmp_active_connection['LocalIP'] = connection.laddr[0]
      tmp_active_connection['ReportDateTime'] = var100
      tmp_active_connection['LocalHostName'] = va1
      if not connection.raddr:
        tmp_active_connection['RemoteIP'] = 'Null'
        tmp_active_connection['Remote-Port'] = 'Null'
      else:
        tmp_active_connection['RemoteIP'] = connection.raddr[0]
        tmp_active_connection['Remote-Port'] = connection.raddr[1]
        cmd_nslook = 'nslookup ' + connection.raddr[0] + '| grep name | cut -d' ' -f3'
        remote_hostname = os.system("cmd_nslook")
        tmp_active_connection['RemoteHostName'] = remote_hostname
    else:
      tmp_active_connection['Connection_Type'] = connection.type
      tmp_active_connection['Local_Port'] = connection.laddr[1]
      tmp_active_connection['LocalIP'] = connection.laddr[0]
      if not connection.raddr:
        tmp_active_connection['RemoteIP'] = 'Null'
        tmp_active_connection['Remote-Port'] = 'Null'
      else:
        tmp_active_connection['RemoteIP'] = connection.raddr[0]
        tmp_active_connection['Remote-Port'] = connection.raddr[1]
        cmd_nslook = 'nslookup ' + connection.raddr[0] + '| grep name | cut -d' ' -f3'
        remote_hostname = subprocess.call('cmd_nslook', shell=True)
        tmp_active_connection['RemoteHostName'] = remote_hostname
    active_connections.append(tmp_active_connection)
  #print active_connections
  return active_connections

connections = get_active_connections()
all = {'active_connections':connections}

print json.dumps(all, indent=4)