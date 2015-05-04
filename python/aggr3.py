import collections
from collections import defaultdict
import ast
from pprint import pprint
import json
import signal
import os
import sys
import traceback
import time

outputParamFile = '..\\json\\params5.json'
inputCSVFile = '..\\tsv\\outFile.tsv'
files = ['C:\\ADMS_DATA\\highway_2014_Jan_Feb_Mar\\h1.txt', \
			'C:\\ADMS_DATA\\highway_2014_Jan_Feb_Mar\\h2.txt', \
			'C:\\ADMS_DATA\\highway_2014_Jan_Feb_Mar\\h3.txt' \
			]
#my_dict = defaultdict(dict)
my_dict2 = {}
my_dict={}
def SigHandler(signal, stack):
	print "SIGINT, partial dictionary written"
	WriteDict()
	traceback.print_stack(stack)
	sys.exit()
	
def CreateInputDict():
	with open(inputCSVFile) as f:
		for x in f:
			s = x.split('|')[2] # get the list of sensors string 
			l = ast.literal_eval(s)	# convert into list
			for y in l:	# for each sensor
				d = {'01':{"10":[],"12":[],"06":[]}, \
	     			  '02':{"03":[],"07":[],"09":[]}, \
					  '03':{"03":[],"07":[],"09":[]}
					  }
					  
				my_dict[y] = d
	
def WriteParams():
	times =  ["%02d" % x for x in range(10, 17)]
	months = ['01', '02', '03']
	for x in files:
	
		with open(x) as f:
	
			for line in f:
				tokens = line.split('|')
			
				if tokens[-1] != 'OK\n':
					continue
								
				timeRead=time.strptime(tokens[2], "%m/%d/%Y %H:%M")
				
				month = "%02d" % (timeRead.tm_mon)
				day = "%02d" % (timeRead.tm_mday)
				
				sensorID = tokens[3]

				if day not in my_dict[sensorID][month].keys():
					continue
					
				hour = "%02d" % (timeRead.tm_hour)

				if hour not in times:
					continue
					
				min = timeRead.tm_min
				
				if min > 0:
					continue;
				
				speedTimeList = my_dict[sensorID][month][day]
				
				if hour in set().union(*(d.values() for d in speedTimeList)):
					continue;
				
				speed = int(tokens[5])
				temp = 	{"time":hour, "speed":speed}	
				speedTimeList.append(temp)
				pprint(temp)
		
				

def SortAll():
	for sensorID in my_dict.keys():
		for month in my_dict[sensorID]:
			for day in my_dict[sensorID][month].keys():
				my_dict[sensorID][month][day] = sorted(my_dict[sensorID][month][day], key=lambda k: int(k['time'])) 
		
def WriteDict():
	#print(my_dict)	
	with open(outputParamFile, 'w') as f:
		json.dump(my_dict, f)	
		
if __name__ == '__main__':
	signal.signal(signal.SIGINT, SigHandler)
	CreateInputDict()
	WriteParams()
	SortAll()
	WriteDict()

