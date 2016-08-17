import csv
import os,sys

def checkExist(filepath):
    if not os.path.exists(filepath):
        open(filepath,'a').close()

l = 0

for i in range(215):
    checkExist('factory_data/p' + str(i + 1) + '.txt')
    fileWrite = open('factory_data/p' + str(i + 1) + '.txt','w')
    count = 1
    csvRead = file('factory_trans.csv', 'rb')
    reader = csv.reader(csvRead)
    for line in reader:
        fileWrite.write('{} '.format(int(line[215])) + \
                        str(count) + ':{}\n'.format(float(line[i])))
        l = len(line)
    fileWrite.close()
    csvRead.close()

for i in range(215):
    checkExist('factory_data/rp' + str(i + 1) + '.txt')
    fileWrite = open('factory_data/rp' + str(i + 1) + '.txt','w')
    count = 1
    csvRead = file('factory_trans.csv', 'rb')
    reader = csv.reader(csvRead)
    for line in reader:
        fileWrite.write('{}'.format(int(line[215])))
        for j in range(l - 1):
            if(j == i):
                continue
            fileWrite.write(' ' + str(count) + ':{}'.format(float(line[j])))
            count += 1
        count = 1
        fileWrite.write('\n')
    fileWrite.close()
    csvRead.close()