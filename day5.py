#!/usr/bin/env python3
import sys

# read file, strip \n
inputs = []
with open(sys.argv[1], 'r') as f:
    inputs = [line.strip() for line in f];

def compute_id(str):
    r = 0
    myrange = [0, 2**(len(str))- 1]
    while myrange[0] < myrange[1]:
        # B / R
        if str[r] in ['B','R']:
            myrange[0] = myrange[0] + (myrange[1] - myrange[0] + 1 ) / 2
        # F / B
        else:
            myrange[1] = myrange[1] - (myrange[1] - myrange[0] + 1 ) / 2
        r = r + 1

    return int(myrange[0])

bpass_ids = [];
for bpass in inputs:
    id = compute_id(bpass[:7]) * 8 + compute_id(bpass[7:])
    bpass_ids.append(id)

print ('Part 1 : %d' % max(bpass_ids))

bpass_ids.sort()
for i in range(0, len(bpass_ids)-1):
    if bpass_ids[i+1] != bpass_ids[i] + 1:
        me = bpass_ids[i] + 1

print ('Part 2 : %d' % me)
