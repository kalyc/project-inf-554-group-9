import sys
import json
import string
import math


def main():

	dict={};
	
	
	with open('hw_config_2014_Jan_Feb_Mar.txt') as f: 
		
		for line in f:
			s=line.split('|')
			s[4]=s[4].strip(" ");
			if s[4] not in dict:
				dict[s[4]]={};
			else:
				continue;
	
	string=''
	with open('sensor_data.txt', 'w') as f1:
		f1.write('{ \n')
		for i in dict.keys():  
			f1.write(str(i) + ":"+ str(dict[i]) + "\n");
		f1.write('}')


if __name__ == '__main__':
	main()