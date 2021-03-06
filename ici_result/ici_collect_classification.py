import csv
import numpy
import os,sys

def collect_nums(filePath):
    res = []
    file = open(filePath, 'r')
    data = file.read()
    data = data.split('\n')
    for line in data:
        if(line.startswith('Cross')):
            res.append(line[28:-1])
    return res

csvRead = file('ici_result_classification.csv', 'rb')
reader = csv.reader(csvRead)

data = []
for line in reader:
    data.append(line)
csvRead.close()

c = [[] for i in range(12)]
c[0] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_linear_05_single')
c[1] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_linear_05_reverse')
c[2] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_linear_1_single')
c[3] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_linear_1_reverse')
c[4] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_linear_5_single')
c[5] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_linear_5_reverse')
c[6] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_rbf_05_single')
c[7] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_rbf_05_reverse')
c[8] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_rbf_1_single')
c[9] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_rbf_1_reverse')
c[10] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_rbf_5_single')
c[11] = collect_nums('/Users/faceOFfact/Desktop/omron_data/ici_result/ici_rbf_5_reverse')
#c = numpy.transpose(c)
#print(len(c),len(c[0]))
c = map(list, zip(*c))
for i in range(27):
    if(i == 26):
        c[i] = ['AB'] + c[i]
        continue
    c[i] = [chr(ord('A') + i)] + c[i]

data = data + c

csvWrite = file('ici_result_classification.csv', 'wb')
writer = csv.writer(csvWrite)
writer.writerows(data)
csvWrite.close()