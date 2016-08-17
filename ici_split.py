import csv
import os,sys

def checkExist(filepath):
    if not os.path.exists(filepath):
        open(filepath,'a').close()

l = 0

for i in range(27):
    checkExist('ici_data/p' + str(i + 1) + '.txt')
    fileWrite = open('ici_data/p' + str(i + 1) + '.txt','w')
    count = 1
    csvRead = file('ici_trans.csv', 'rb')
    reader = csv.reader(csvRead)
    for line in reader:
        fileWrite.write('{} '.format(int(line[27])) + \
                        str(count) + ':{}\n'.format(float(line[i])))
        l = len(line)
    fileWrite.close()
    csvRead.close()

for i in range(27):
    checkExist('ici_data/rp' + str(i + 1) + '.txt')
    fileWrite = open('ici_data/rp' + str(i + 1) + '.txt','w')
    count = 1
    csvRead = file('ici_trans.csv', 'rb')
    reader = csv.reader(csvRead)
    for line in reader:
        fileWrite.write('{}'.format(int(line[27])))
        for j in range(l - 1):
            if(j == i):
                continue
            fileWrite.write(' ' + str(count) + ':{}'.format(float(line[j])))
            count += 1
        count = 1
        fileWrite.write('\n')
    fileWrite.close()
    csvRead.close()