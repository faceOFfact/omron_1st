import csv
import os,sys

def checkExist(filepath):
    if not os.path.exists(filepath):
        open(filepath,'a').close()

l = 0
'''
for i in range(27):
    if(i == 10 or i == 13 or i == 21):
        continue
    checkExist('ici_data_s2/p' + str(i + 1) + '.txt')
    fileWrite = open('ici_data_s2/p' + str(i + 1) + '.txt','w')
    count = 1
    csvRead = file('ici_trans.csv', 'rb')
    reader = csv.reader(csvRead)
    for line in reader:
        fileWrite.write('{}'.format(int(line[27])))
        fileWrite.write(' 1:{}'.format(float(line[10])))
        fileWrite.write(' 2:{}'.format(float(line[13])))
        fileWrite.write(' 3:{}'.format(float(line[21])))
        fileWrite.write(' 4:{}'.format(float(line[i])))
        fileWrite.write('\n')
    fileWrite.close()
    csvRead.close()
'''
checkExist('ici_data_s2/pl.txt')
fileWrite = open('ici_data_s2/pl.txt','w')
csvRead = file('ici_trans.csv', 'rb')
reader = csv.reader(csvRead)
for line in reader:
    fileWrite.write('{}'.format(int(line[27])))
    fileWrite.write(' 1:{}'.format(float(line[12])))
    fileWrite.write(' 2:{}'.format(float(line[13])))
    fileWrite.write(' 3:{}'.format(float(line[21])))
    #fileWrite.write(' 4:{}'.format(float(line[11])))
    #fileWrite.write(' 5:{}'.format(float(line[12])))
    fileWrite.write('\n')
fileWrite.close()
csvRead.close()