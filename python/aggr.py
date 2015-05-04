with open('readings_716466_sorted.txt') as f:
	d = {'01':{'speed':0, 'count': 0}, '02':{'speed':0, 'count': 0}, '03':{'speed':0, 'count': 0}}
	dOut = {}
	#Jan
	for line in f:
		tokens = line.split('|')
		month = tokens[2].split('/')[0]
		d[month]['speed'] += int(tokens[5])
		d[month]['count'] += 1
		
	for key in d:
		dOut[key] = d[key]['speed'] / d[key]['count'] 
	
print dOut
