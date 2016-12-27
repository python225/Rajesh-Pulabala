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

partions = psutil.disk_partitions()
dev_to_mnt_point_dict = {}
dev_to_disk_space = {}
devices = []
mount_points = []
output = {}

for partion in partions:
  #print partion.device
  dev_to_mnt_point_dict[partion.device] = partion.mountpoint

for dev, mnt_point in dev_to_mnt_point_dict.iteritems():
  usage = psutil.disk_usage(mnt_point)
  total_disk = usage.total
  usage_percent = usage.percent
  mnt_point_dict = {}
  disk_dict = {}
  used_per_dict = {}
  mnt_point_dict['mount_point'] = mnt_point  
  disk_dict['Total_disk'] = total_disk
  used_per_dict['Percent_used'] = usage_percent
  disk_stats = [mnt_point_dict,disk_dict,used_per_dict]
  dev_to_disk_space['DeviceID: '+dev] = disk_stats

#print json.dumps(dev_to_disk_space, indent=2)




#1) for getting DNS Host Name 
def get_dna():
    name = subprocess.check_output("hostname | cut -d'.' -f1", shell=True)
    return name
var1 = get_dna()
#1) for getting DNS Host Name 
def get_dom():
    nam = subprocess.check_output("hostname | cut -d'.' -f2", shell=True)
    return nam
va1 = get_dom()


# 2)For getting manufacture details of the current running system

def get_mani():
      manuf = subprocess.check_output("dmidecode | grep Manufacturer | sed -n '1p'", shell=True)
      return manuf
var2 = get_mani()

# 3)For getting model of the current running system

def get_mod():
       model = os.system("dmidecoder | grep Model")
       return model
var3 = get_mod()

# 4) For getting the number of logical processors

def get_proc1():
       totl = psutil.cpu_count()
       return totl
var4 = get_proc1()


# 5) For getting the Number of processers in system

def get_proc2():
       physical = psutil.cpu_count(logical=False)
       return physical
var5 = get_proc2()

# 6) For getting operating system description

def get_des():
       dis = platform.platform()
       return dis
var6 = get_des()


# 7) For getting productname

def get_pro():
       a = subprocess.check_output("dmidecode | grep Product | head -1 | awk '{print$3}'", shell=True)
       return a
var7 = get_pro()


# 8) For getting Vendor of the system

def get_vend():
      b = subprocess.check_output("dmidecode | grep Vendor", shell=True)
      return b
var8 = get_vend()

# 9) for getting Version

def get_ver():
       c = subprocess.check_output("dmidecode | grep Version | sed -n '2p'", shell=True)
       return c
var9 = get_ver()

# for getting processor

def get_pr():
      d = platform.processor()
      return d
var10 = get_pr()


#For getting systemos

def get_os():
      sys = platform.system()
      return sys
var11 = get_os() 



#For getting ip address 


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ip_Address = get_ip_address('eth0')



def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

def get_dhc():
  aa = subprocess.check_output("cat /var/lib/dhclient/dhclient.leases | grep server-identifier | awk '{print$3}'", shell=True)
  return aa
vari = get_dhc()

def get_netmask(ifname):
  #  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   # info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    addrs = netifaces.ifaddresses(ifname)
    ipinfo = addrs[socket.AF_INET][0]
#    print ipinfo
    netmask = ipinfo['netmask']
    return netmask

def get_fqdn():
    fqdn = socket.getfqdn()
    return fqdn
FQD_name = get_fqdn() 
#print "Fully Qualified Domain Name:", FQD_name
netmask_Addr=get_netmask('eth0')
ip_mac_Address = getHwAddr('eth0')
val=netifaces.interfaces()
value=netifaces.ifaddresses(val[0])


allcontent= {'DomainName':va1,'Disks':dev_to_disk_space,'DNSHostName':var1,'Manufacturer':var2,'Model': var3,'NumberOfLogicalProcessors':var4,'NumberOfProcessors': var5,'OperatingSystem':[{'Description':var6,'ProductName':var7,'Vendor':var8,'Version':var9,'Processor':var10,'System OS':var11}], 'Nics':[{'IPAddress':ip_Address,'DHCPServerIPAddress':vari,'DNSDomain':FQD_name,'MACAddress':ip_mac_Address,'SubnetMask':netmask_Addr}]}

print json.dumps(allcontent, indent=4)