#import sys
l = []
#sensorID = sys.argv[1]
#print sensorID
#path = '/home/abhi/Downloads/ADMS_DATA/highway_2014_Jan_Feb_Mar/'
#files = ['h1.txt']

#for f in files:
#	sensorReadings = []
#	with open(path + f, 'r') as inFile:
#		print 'aaa'
#		for line in inFile:			
#			if line.endswith('OK') and sensorID in line:
#				sensorReadings.append(line)
#				print sensorReadings
#		with open('readings_' + sensorID + '.txt', 'w+') as outFile:
#			outFile.writelines(sensorReadings)
		


with open('readings_716956.txt', 'r') as f: #'readings_716466.txt'
	l = f.readlines()
	l.sort()
with open('readings_716956_sorted.txt', 'w') as f:
	f.writelines(l)
