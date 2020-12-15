#!/usr/bin/env python3
import sys

def to_int(string):
    return int(string)

# read file, convert strings to integers
inputs = []
with open(sys.argv[1], 'r') as f:
    inputs = list(map(to_int, f.readline().split(',')))

# keep original input for part 2
numbers = inputs.copy()

# naive approach for part 1

i = len(numbers)
while i < 2020:
    last_spoken = numbers[i-1]
    if last_spoken in (numbers[:i-1]):
        rlist = numbers.copy()
        rlist.reverse()
        idx = rlist[1:].index(last_spoken)
        numbers.append(idx + 1)
    else:
        numbers.append(0)
    i = i + 1

print ('Part 1 : %d' % numbers[-1])

number_pos = dict()

# for part 2 we have to be more clever
# don't copy/search lists, but keep track of number indices

# keep all starting number positions *but* last one
for i in range(0, len(inputs)-1):
    number_pos[inputs[i]] = i

i = i + 1
while i < 30000000 - 1:
    last_spoken = inputs[i]
    if last_spoken in number_pos:
        inputs.append(i-number_pos[last_spoken])
        number_pos[last_spoken] = i
    else:
        inputs.append(0)
        number_pos[last_spoken] = i
    i = i + 1

print ('Part 2 : %d' % inputs[-1])
