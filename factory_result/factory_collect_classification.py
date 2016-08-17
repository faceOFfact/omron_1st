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

def convertToTitle(n):
    res = ''
    while(n > 0):
        t = n % 26
        off = 0
        if(t == 0):
            t = 26
            off = 1
        res = chr(t + 64) + res
        n /= 26
        n -= off
    return res

csvRead = file('factory_result_classification.csv', 'rb')
reader = csv.reader(csvRead)

data = []
for line in reader:
    data.append(line)
csvRead.close()

c = [[] for i in range(12)]
c[0] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_linear_05_single')
c[1] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_linear_05_reverse')
c[2] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_linear_1_single')
c[3] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_linear_1_reverse')
c[4] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_linear_5_single')
c[5] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_linear_5_reverse')
c[6] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_rbf_05_single')
c[7] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_rbf_05_reverse')
c[8] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_rbf_1_single')
c[9] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_rbf_1_reverse')
c[10] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_rbf_5_single')
c[11] = collect_nums('/Users/faceOFfact/Desktop/omron_data/factory_result/factory_rbf_5_reverse')
#c = numpy.transpose(c)
#print(len(c),len(c[0]))
c = map(list, zip(*c))
for i in range(215):
    c[i] = [convertToTitle(i + 1)] + c[i]

data = data + c

csvWrite = file('factory_result_classification.csv', 'wb')
writer = csv.writer(csvWrite)
writer.writerows(data)
csvWrite.close()