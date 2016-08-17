import csv
import os,sys
import re

nums = []
file = open('ici_linear_1_single')
data = file.read()
data = data.split('\n')
for line in data:
    if(line.startswith('Cross')):
        nums.append(line[28:-1])

print(nums)