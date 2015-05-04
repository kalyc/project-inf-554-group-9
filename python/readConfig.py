from collections import defaultdict

my_dict = defaultdict(set)


with open('/home/abhi/Downloads/ADMS_DATA/hw_config_2014_Jan_Feb_Mar.txt', 'r') as f:
	count = 0
	for line in f:
		ll = [x.strip() for x in line.split('|')]
		#key = (ll[6], ll[4])
		highway = ll[6]
		sensorID = ll[4]
		
		
		my_dict[highway].add(sensorID)
		#print "COUNT!!!!!", count
		count += 1

#for w in sorted(my_dict, key=my_dict.get, reverse=True):
#	print w, my_dict[w]

with open('outFile.csv', 'w') as f:
	for x in my_dict:
		s = x + "|" + str(len(my_dict[x])) + "|" + str(my_dict[x]) + "\n"
		f.write(s)
