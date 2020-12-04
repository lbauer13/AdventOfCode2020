#!/usr/bin/env python3
import sys

# read file, strip \n
lines = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        row = list(line.strip())
        lines.append(row)

def slope(right, down):
    count = 0
    y = 0
    i = 0
    while y < len(lines) - 1:
        i = i + 1
        y = y + down
        x = right * i % len(lines[y])
        if (lines[y][x] == '#'):
            count = count + 1
    return count

print ('Part 1 : %d' % slope(3, 1))
print ('Part 2 : %d'% (slope(1,1) * slope(3,1) * slope(5,1) * slope(7,1) * slope(1,2)))
