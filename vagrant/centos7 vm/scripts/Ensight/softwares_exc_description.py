#!/usr/bin/python

import subprocess
import json



cmd = "yum list installed | sed -e '1,/Installed/d'"



#def get_soft():


list_of_sw = subprocess.check_output(cmd,shell=True)
software_to_version = {}
software_to_vendor = {}
software_to_description = {}
software_to_version_vendor = {}
softwares = []
for i in list_of_sw.split('\n'):
	tmp_list = i.split()
	if len(tmp_list) == 3:
		softwares.append(tmp_list[0])
		software_to_vendor[tmp_list[0]] = tmp_list[2]
		software_to_version[tmp_list[0]] = tmp_list[1]

for software in softwares:
	version_vendor_list = []
	version_vendor_list = [{'version':software_to_version[software]},{'vendor':software_to_vendor[software]}]
	software_to_version_vendor['product_name: ' +  software]=version_vendor_list
#    return software_to_version_vendor
#va = get_soft()
print json.dumps(software_to_version_vendor, indent=4)