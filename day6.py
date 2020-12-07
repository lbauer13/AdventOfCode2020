#!/usr/bin/env python3
import sys

# read file, strip \n
groups = []
with open(sys.argv[1], 'r') as f:
    data = []
    for line in f:
        if line.rstrip() == '':
            groups.append(data)
            data = []
        else:
            data.append(line.rstrip())

questions = []
for g in groups:
    d = dict()
    for answer in g:
        for letter in list(answer):
            if letter in d.keys():
                d[letter] = d[letter] + 1
            else:
                d[letter] = 1
    questions.append(d)

sum1 = 0
for q in questions:
    sum1 = sum1 + len(q)

print ('Part 1 : %d' % sum1)

sum2 = 0
for i in range(0, len(groups)):
    sub = 0
    for j, (k,v) in enumerate(questions[i].items()):
        if v == len(groups[i]):
            sub = sub + 1
    sum2 = sum2 + sub

print ('Part 2 : %d' % sum2)
