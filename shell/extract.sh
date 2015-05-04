#!/bin/bash

echo $1
f1="readings_$1_h1.txt"
echo $f1
awk "/$1.*OK$/" /home/abhi/Downloads/ADMS_DATA/highway_2014_Jan_Feb_Mar/h1.txt > $f1
echo 'h1 written'

f2="readings_$1_h2.txt"
awk "/$1.*OK$/" /home/abhi/Downloads/ADMS_DATA/highway_2014_Jan_Feb_Mar/h2.txt > $f2
echo 'h2 written'

f3="readings_$1_h3.txt"
awk "/$1.*OK$/" /home/abhi/Downloads/ADMS_DATA/highway_2014_Jan_Feb_Mar/h3.txt > $f3
echo 'h3 written'

f4=readings_$1.txt
cat $f1 $f2 $f3 > $f4

rm $f1
rm $f2
rm $f3


