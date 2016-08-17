#!/bin/sh

for i in {1..27}
do
    filename='rp'${i}'.txt'
    #echo $filename
    echo '-----------------'${i}'-----------------'
    ./libsvm-3.21/svm-train -t 2 -v 5 -q -c 5 ici_data/$filename
done