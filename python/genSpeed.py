import random
m = {"02":{  \
         "vol":0,\
         "speed":0\
      },\
      "03":{  \
         "vol":0,\
         "speed":0\
      },\
      "01":{  \
         "vol":0,\
         "speed":0\
      }}
sensors = [716958,716956,716955,716953,716951,716949,716946,716944,716943,716942,716941,716940,716939,716938,716907,716906,716904,716902,716901,716900,716899,716898,716896,716895]
print sensors
d={}
#speeds = random.sample(xrange(50,60), len(sensors) * 3)
#vols = random.sample(xrange(1,10), len(sensors) * 3)
speeds = []
vols = []
i = 0
random.seed()
j = 50
v = 1
while i < (len(sensors) * 3):
	speeds.append(j)
	vols.append(v)
	j += 0.5
	v += 0.5
	i += 1
i = 0
j = 50
v = 1
for x in sensors:
	for k in m:
		kk = speeds[i]
		m[k]['speed'] = j#kk#float("%.2f" % kk)
		kk = vols[i]
		m[k]['vol'] = v#kk#float("%.2f" % kk)
		j += 0.5
		v += 0.5
		i += 1
	d[x] = m
from pprint import pprint
pprint(d)
