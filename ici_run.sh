#!/bin/sh

for i in {1..27}
do
    filename='rp'${i}'.txt'
    #echo $filename
    echo '-----------------'${i}'-----------------'
    ./libsvm-3.21/svm-train -s 4 -v 5 -q ici_data/$filename
done