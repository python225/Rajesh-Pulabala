#!/usr/bin/python
import subprocess
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


new_nic_list = get_nics()


print new_nic_list

for new_nic in new_nic_list:
    new_correct_nic = new_nic.replace(':',"")
    #print new_correct_nic

    cmd = 'ifconfig ' + new_correct_nic

    output_ifconfig = subprocess.check_output(cmd,shell=True)

    output_ifconfig_list = output_ifconfig.split('\n\n')

    mac_rx_tx = []

    for output_line in output_ifconfig_list:
            nic_line_list = output_line.splitlines()
            for line in nic_line_list:
                    #print line
                    if 'inet' in line and ('netmask' in line):
                    	dict_inet_nmsk_broadcast = {}
                        list_inet_line = line.split()
                        dict_inet_nmsk_broadcast[list_inet_line[0]] = str(list_inet_line[1])
                        dict_inet_nmsk_broadcast[list_inet_line[2]] = str(list_inet_line[3])
                        if 'inet' in line and ('netmask' in line) and  ('broadcast' in line):
                             dict_inet_nmsk_broadcast[list_inet_line[4]] = str(list_inet_line[5])
                        mac_rx_tx.append(dict_inet_nmsk_broadcast)
                    if 'ether' in line:
                        dict_ether_mac = {}
                        ether_mac_line = line.split()
                        dict_ether_mac[ether_mac_line[0]] = str(ether_mac_line[1])
                        mac_rx_tx.append(dict_ether_mac)


                    if 'RX' in line and ('packets' in line):
                            #print line
                        rx_bytes = {}
                        rx_bytes_line = line.split()
                        rx_bytes[rx_bytes_line[0]+'_'+rx_bytes_line[3]] = rx_bytes_line[4]
                        mac_rx_tx.append(rx_bytes)
                    if 'TX' in line and ('packets' in line):
                            #print line
                        tx_bytes = {}
                        tx_bytes_line = line.split()
                        tx_bytes[tx_bytes_line[0]+'_'+tx_bytes_line[3]] = tx_bytes_line[4]
                        mac_rx_tx.append(tx_bytes)
    #print mac_rx_tx
    dict_nics_info[new_correct_nic] = mac_rx_tx
print json.dumps(dict_nics_info,indent = 4)