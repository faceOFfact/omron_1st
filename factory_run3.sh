#!/bin/sh

for i in {1..215}
do
    filename='rp'${i}'.txt'
    #echo $filename
    echo '-----------------'${i}'-----------------'
    ./libsvm-3.21/svm-train -v 5 -q -c 5 factory_data/$filename
done