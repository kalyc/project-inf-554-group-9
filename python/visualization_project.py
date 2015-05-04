import sys
import json
import string
import math


def main():
#s= ' ';
	list=[];
	lat_long='';
	lat='';
	long='';
	line=None
	with open('highway_lat_long.json', 'w') as f1:
		f1.write('{\n')
		f1.write('"type": "FeatureCollection",\n')
		f1.write('"features": [ \n')
		sensor_id=set()
		with open('hw_config_2014_Jan_Feb_Mar.txt') as f: 
			lines = f.readlines()
			last = lines[-1]
			for line in lines[:-2]:
		#	for line in f:
				s=line.split('|')
				sensor_id.add(s[4])
				if s[4] in sensor_id:
				

					lat_long=s[9].split(',')
					lat= lat_long[2]
					long=lat_long[3]
					x=float(lat[16:])
					y=float(long)
					f1.write('\t{\n')
					f1.write('\t\t"type": "Feature",\n')
					
					f1.write('\t\t"properties": { "ID":'+ s[4].strip(" ")+','
												+'"Highway":'+'"'+s[6].strip(" ")+'"'+
													'}, \n')
					f1.write('\t\t"geometry": {\n')
					f1.write('\t\t\t"type": "Point",\n')
					f1.write('\t\t\t"coordinates": [\n')
					f1.write(str(x))
					f1.write(',')
					f1.write(str(y))
					f1.write('\n')
					f1.write('\t\t\t]\n')
					f1.write('\t\t}\n')
					f1.write('\t}')
					f1.write(',\n')
					
				else:
				
					continue;
				
				
		line=lines[-1]
		s=line.split('|')
		#s.split('|')

		lat_long=s[9].split(',')
		lat= lat_long[2]
		long=lat_long[3]
		sensor_id.add(s[4])
		if s[4] in sensor_id:
		
			f1.write('\t{\n')
			f1.write('\t\t"type": "Feature",\n')
			f1.write('\t\t"properties": { "ID":'+ s[4].strip(" ")+','
												+'"Highway":'+'"'+s[6].strip(" ")+'"'+
													'}, \n')
			f1.write('\t\t"geometry": {\n')
			f1.write('\t\t\t"type": "Point",\n')
			f1.write('\t\t\t"coordinates": [\n')
			f1.write('\t\t\t'+lat[16:] +','+ '\n')
			f1.write('\t\t\t'+long+'\n') 
			f1.write('\t\t\t]\n')
			f1.write('\t\t}\n')
			f1.write('\t}\n')
			f1.write('\t]\n')
			f1.write('}\n')
		
	print(sensor_id)
	f.close()
	f1.close()
"""
mystr = '\t'.join([line.strip() for line in config_])
"""	



if __name__ == '__main__':
	main()