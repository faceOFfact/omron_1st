import csv
import numpy
import os,sys

def collect_nums(filePath):
    res = []
    res1 = []
    file = open(filePath, 'r')
    data = file.read()
    data = data.split('\n')
    for line in data:
        if(line.startswith('Cross Validation Mean')):
            res.append(line[38:])
        if(line.startswith('Cross Validation Squared')):
            res1.append(line[51:])
    return res, res1

csvRead = file('ici_result_regression.csv', 'rb')
reader = csv.reader(csvRead)

data = []
for line in reader:
    data.append(line)
csvRead.close()
#print(data)

c = [[] for i in range(8)]
c[0], c[1] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_regression_s3_single')
c[2], c[3] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_regression_s3_reverse')
c[4], c[5] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_regression_s4_single')
c[6], c[7] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_regression_s4_reverse')
#c = numpy.transpose(c)
#print(len(c),len(c[0]))
c = map(list, zip(*c))
#print(c)
for i in range(27):
    if(i == 26):
        c[i] = ['AB'] + c[i]
        continue
    c[i] = [chr(ord('A') + i)] + c[i]

data = data + c

csvWrite = file('ici_result_regression.csv', 'wb')
writer = csv.writer(csvWrite)
writer.writerows(data)
csvWrite.close()