#!/bin/sh

for i in {1..215}
do
    filename1='p'${i}'.txt'
    filename2='rp'${i}'.txt'
    #echo $filename
    echo '-----------------'${i}'-----------------'
    python ../libsvm-3.21/tools/checkdata.py $filename1
    python ../libsvm-3.21/tools/checkdata.py $filename2
done