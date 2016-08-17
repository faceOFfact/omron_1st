import csv

csvRead = file('ici.csv', 'rb')
reader = csv.reader(csvRead)
csvWrite = file('ici_trans.csv', 'wb')
writer = csv.writer(csvWrite)

data = []
for line in reader:
    if(line[0] == 'X_Minimum'):
        continue
    l = len(line)
    lineData = []
    for i in range(l - 7):
        lineData.append(float(line[i]))
    s = 0
    for i in range(l - 7, l):
        if(line[i] == '1'):
            lineData.append(i - l + 8)
#s += int(line[i]) * (2**(i - l + 7))
    data.append(lineData)

writer.writerows(data)

csvRead.close()
csvWrite.close()