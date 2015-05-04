from collections import defaultdict
import ast
from pprint import pprint
import json
import signal
import os
import sys
import traceback

outputParamFile = '/home/abhi/Code/infoviz/json/params.json'
inputCSVFile = '/home/abhi/Code/infoviz/csv/outFile.csv'
files = ['/home/abhi/Downloads/ADMS_DATA/highway_2014_Jan_Feb_Mar/h1.txt', \
			'/home/abhi/Downloads/ADMS_DATA/highway_2014_Jan_Feb_Mar/h2.txt', \
			'/home/abhi/Downloads/ADMS_DATA/highway_2014_Jan_Feb_Mar/h3.txt']
my_dict = defaultdict(dict)

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
				d = {'01':{'speed':0.0, 'vol': 0.0, 'occ': 0.0, 'count': 1}, \
					  '02':{'speed':0.0, 'vol': 0.0, 'occ': 0.0, 'count': 1}, \
					  '03':{'speed':0.0, 'vol': 0.0, 'occ': 0.0, 'count': 1}}
					  
				my_dict[y] = d
			
def WriteParams():
	for x in files:
	
		with open(x) as f:
	
			for line in f:
				tokens = line.split('|')
			
				if tokens[-1] != 'OK\n':
					continue
				
				sensorID = tokens[3]
				month = tokens[2].split('/')[0]
			
				occupancy = float(tokens[4])
				speed = float(tokens[5])
				vol = float(tokens[6])
				
				#if sensorID in my_dict:
				d = my_dict[sensorID][month]
			
				# Speed
				d['speed'] = (d['speed'] * (d['count'] - 1) / d['count']) + (speed / d['count'])# / d['count']
				#d['speed'] /= d['count']
			
				# Volume
				d['vol'] = (d['vol'] * (d['count'] - 1) / d['count']) + (vol / d['count'])# / d['count']
				#d['vol'] /= d['count']
			
				# Occupancy
				d['occ'] = (d['occ'] * (d['count'] - 1) / d['count']) + (occupancy / d['count'])# / d['count']
				#d['occ'] /= d['count']
				# Increase count
				d['count'] += 1
				
				#print sensorID
				#if sensorID == '770747':
				#	print speed
				#pprint(d)
	
def RemoveCount():		
	for sensorID in my_dict:
		for month in my_dict[sensorID]:
			my_dict[sensorID][month].pop("count", None)

def WriteDict():
	with open(outputParamFile, 'w') as f:
		json.dump(my_dict, f)	
		
if __name__ == '__main__':
	signal.signal(signal.SIGINT, SigHandler)
	CreateInputDict()
	WriteParams()
	RemoveCount()
	WriteDict()

