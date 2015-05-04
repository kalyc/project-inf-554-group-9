import json
sensorDict = {}

with open('/home/abhi/Code/infoviz/json/sensor_data.json', 'r') as f:
	sensorDict = json.load(f)

with open('/home/abhi/Code/infoviz/json/params.json', 'r') as f:
	paramDict = json.load(f)
	
	
from pprint import pprint


for x in sensorDict:
	sensorDict[x]['params'] = paramDict[x]
#pprint(sensorDict)

with open('/home/abhi/Code/infoviz/json/sensor_data2.json', 'w') as f:
	json.dump(sensorDict, f)

