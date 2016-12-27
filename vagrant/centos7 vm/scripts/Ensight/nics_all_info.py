#!/usr/bin/python

import netifaces
import json
import socket
import fcntl
import struct

dict_nics_info = {}

def get_nics():
    cmd_ifconfig_1="ifconfig -a | sed 's/[ \t].*//;/^$/d'"
    str_of_nics = subprocess.check_output(cmd_ifconfig_1, shell=True)
    list_of_nics = str_of_nics.splitlines()
    return list_of_nics


 def all_nics_info_data():

    list_of_nics_var = get_nics()


    for nic in list_of_nics_var:
        act_nic = nic.replace(':',"")
        print act_nic
        list_of_nic_info = []
        list_of_nic_info.append('IPAddress: ' + str(get_ip_address(act_nic))
        list_of_nic_info.append('SubnetMask: ' + str(get_netmask(act_nic)))
        dict_nics_info['Nic: ' + act_nic] = list_of_nic_info

    return json.dumps(dict_nics_info)