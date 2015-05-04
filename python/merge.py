geoDict = {}
propDict = {}
import json
geoFile = 'short-data.json'
outFile = 'short-data2.json'
paramsFile = 'json/speeds.json'
with open(geoFile, 'r') as f:
	geoDict = json.load(f)
with open(paramsFile, 'r') as f:
	propDict = json.load(f)
	
from pprint import pprint
pprint(geoDict)
#pprint(propDict)

#for key in propDict:
#	geoDict['features']
newlist = sorted(geoDict['features'], key=lambda k: k['properties']['ID'])
geoDict['features'] = newlist

#pprint(geoDict)

def SearchAndInsert(featureList, key, low, high):
	mid = (low + high) / 2;
	
	if featureList[mid]['properties']['ID'] == key:
		print 'yessss'
		featureList[mid]['properties']['params'] = propDict[str(key)]
		return
	elif key < featureList[mid]['properties']['ID']:
		SearchAndInsert(featureList, key, low, mid)
	else:
		SearchAndInsert(featureList, key, mid + 1, high)

for key in propDict:
	SearchAndInsert(geoDict['features'], int(key), 0, len(geoDict['features']))
	#for pointDict in geoDict['features']:
	#	if pointDict['properties']['ID'] == int(key):
	#		pointDict['properties']['params'] = propDict[key]

#pprint(geoDict)
with open(outFile, 'w') as f:
	json.dump(geoDict, f)
