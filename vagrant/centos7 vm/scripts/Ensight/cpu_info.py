#!/usr/bin/python


import psutil
import multiprocessing
import json
import os
import platform



virtual_memory = psutil.virtual_memory()

swap_memory = psutil.swap_memory()

#Total_cpu_count = psutil.cpu_count()

#physical_cpu = psutil.cpu_count(logical=False)


output = { 
	
	'virtual_memory':{
                'total': virtual_memory.total,
		'available':virtual_memory.available,
		'percent_used' : virtual_memory.percent
	},

         'swap_memory':{
		'total': swap_memory.total,
	#	'available': swap_memory.available,
		'percent_used' :swap_memory.percent
        },

#	'Total_cpu_count':{
#		   'total': Total_cpu_count
 #       },
#
 #        'Physical_cpu' : {
  #                  'total' : physical_cpu
 #       },
#
}
print json.dumps(output, indent=4)

