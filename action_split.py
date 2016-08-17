import csv
import os,sys
from itertools import combinations

def checkExist(filepath):
    if not os.path.exists(filepath):
        open(filepath,'a').close()

comb = []
for i in range(1, 7):
    comb = comb + list(combinations([1,2,3,4,5,6], i))

count = len(comb)
#print(count)
#total number of files
for i in range(count):
    name = ''
    for j in range(len(comb[i])):
        name = name + str(comb[i][j])
    #print(name)
    checkExist('action_data/p' + name + '.txt')
    fileWrite = open('action_data/p' + name + '.txt','w')
    csvRead = file('action3.csv', 'rb')
    reader = csv.reader(csvRead)

#l = len(comb[i])
    for line in reader:
        fileWrite.write('{}'.format(int(line[0])))
        for j in range(1, 7):
            if(j in comb[i]):
                fileWrite.write(' ' + str(count) + ':{}'.format(float(line[j])))
                count += 1
        count = 1
        fileWrite.write('\n')
    fileWrite.close()
    csvRead.close()
