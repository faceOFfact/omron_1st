import csv

def convert(s):
    sum = 0
    index = 1
    length = len(s)
    for i in reversed(range(length)):
        sum  = sum + index * (ord(s[i]) - 64)
        index = index * 26
    return sum - 1

csvRead = file('factory.csv', 'rb')
reader = csv.reader(csvRead)

dataValid = 0
data = []
for line in reader:
    if(line[24] != 'NA' and line[24] != 'CONFIRM_RESULT_CODE'):
        dataValid += 1
        data.append(line)

for i in range(dataValid):
    data[i].append(data[i][24])
    data[i][24] = 0
#del(data[i][24])

check = []
l = len(data[0])
for i in range(l):
    flag = True
    for j in range(dataValid):
        if(data[j][i] != data[0][i]):
            flag = False
    check.append(flag)

dataWrite = []
for i in range(dataValid):
    temp = []
    for j in range(l):
        if(j == l - 1):
            if(data[i][j] != '0'):
                temp.append(-1)
            else:
                temp.append(1)
            continue
    
        if(convert('G') == j):
            data[i][j].replace('-', '.')
            data[i][j].replace('_', '')
        if(convert('X') == j or convert('Z') == j or convert('AL') == j or convert('AM') == j \
           or convert('AW') == j or convert('AX') == j or convert('BM') == j or convert('EQ') == j \
           or convert('FA') == j or convert('GG') == j):
            data[i][j] = 0
        if(convert('AD') == j):
            data[i][j] = data[i][j][-2:]
        if(convert('AJ') == j or convert('AK') == j):
            data[i][j] = float(data[i][j][:2])*60 + float(data[i][j][3:])
        if(convert('G') == j or convert('AO') == j or convert('AU') == j or convert('AY') == j \
           or convert('EP') == j or convert('EZ') == j or convert('GF') == j):
            data[i][j] = data[i][j].replace('-', '').replace('_', '')
           #data[i][j].replace('_', '')
        if(convert('AR') == j or convert('AS') == j):
            data[i][j] = 1
        if(convert('FU') == j or convert('FW') == j or convert('FX') == j):
            if(data[i][j] == '(1.00)'):
                data[i][j] = 1
            else:
                data[i][j] = 0
        if(convert('S') == j):
            if(data[i][j].startswith('10088U')):
                data[i][j] = 1
            else:
                data[i][j] = 0

        if(check[j] == True):
            temp.append(0)
        else:
            if(data[i][j] != 'NA'):
                temp.append(data[i][j])
            else:
                temp.append(-1)
    dataWrite.append(temp)

csvWrite = file('factory_trans.csv', 'wb')
writer = csv.writer(csvWrite)
writer.writerows(dataWrite)

csvRead.close()