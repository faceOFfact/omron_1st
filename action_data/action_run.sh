#!/bin/sh

function scan(){
    for file in `ls $1`
    do
        echo '--------------------'$file'--------------------'
        ../libsvm-3.21/svm-train -t 0 -c 5 -v 5 -q $file
    done
}
INIT_PATH = "/Users/faceOFfact/Desktop/omron_data/action_data/"
scan $INIT_PATH