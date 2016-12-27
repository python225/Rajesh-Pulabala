#!/usr/bin/python

import netifaces
import json
import socket
import fcntl
import struct
def get_nics():
    cmd_ifconfig_1="ifconfig -a | sed 's/[ \t].*//;/^$/d'"
    str_of_nics = subprocess.check_output(cmd_ifconfig_1, shell=True)
    list_of_nics = str_of_nics.splitlines()
    return list_of_nics


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ip_Address = get_ip_address('eth0')
'''def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]'''

def get_netmask(ifname):
  #  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   # info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    addrs = netifaces.ifaddresses(ifname)
    ipinfo = addrs[socket.AF_INET][0]
    print ipinfo
    netmask = ipinfo['netmask']
    return netmask
def gethostname():
    hostname = socket.gethostname()
    return hostname
DNS_Hostname= gethostname()
print "DNSHostName:",DNS_Hostname

def getfqdn():
    fqdn = socket.getfqdn()
    return fqdn
FQD_name= getfqdn() 
print "Fully Qualified Domain Name:", FQD_name
netmask_Addr=get_netmask('eth0')
ip_mac_Address = getHwAddr('eth0')
val=netifaces.interfaces()
value=netifaces.ifaddresses(val[0])
print ip_mac_Address
print ip_Address
print netmask_Addr

allcontent= {'Nics':[{'IPAddress':ip_Address,'MACAddress':ip_mac_Address,'SubnetMask':netmask_Addr}]}
print allcontent

print json.dumps(allcontent)
