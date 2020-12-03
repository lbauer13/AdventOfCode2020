#!/usr/bin/python3
import sys
import re

# read file, strip \n
inputs = []
with open(sys.argv[1], 'r') as f:
    inputs = [line.strip() for line in f];

count_ok_1 = 0
count_ok_2 = 0
for line in inputs:
    m = re.search('(.*)-(.*) (.*): (.*)', line)
    m1 = int(m.group(1))
    m2 = int(m.group(2))

    # part 1
    newpwd = re.sub('[^'+m.group(3)+']', '', m.group(4))
    if len(newpwd) >= m1 and len(newpwd) <= m2:
        count_ok_1 = count_ok_1 + 1

    # part 2
    pwd = list(m.group(4))
    # lazy xor
    if (pwd[m1 - 1] == m.group(3) or pwd[m2 - 1] == m.group(3)) and (pwd[m1 - 1] != pwd[m2 - 1]):
        count_ok_2 = count_ok_2 + 1

print ('Part 1 : %d' % count_ok_1)

print ('Part 2 : %d' % count_ok_2)
