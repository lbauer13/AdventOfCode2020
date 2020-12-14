#!/usr/bin/env python3
import sys

# read file, convert strings to integers
departure = 0
busses = []
numbered_busses = []
with open(sys.argv[1], 'r') as f:
    departure = int(f.readline().rstrip())
    i = 0
    for b in f.readline().rstrip().split(','):
        if b == 'x':
            busses.append(b)
        else:
            busses.append(int(b))
            numbered_busses.append(int(b))
        i = i + 1

wait_times = dict()

for b in busses:
    if b != 'x':
        wait_times[b] = b - int(departure % b)

first_to_leave = min(wait_times, key=wait_times.get)

print('Part 1 : %d' % (first_to_leave * wait_times[first_to_leave]))

found = False
step = numbered_busses[0]
max_count = 0

time = 0
while not found:
    time = time + step
    # consider all offsets match
    # and set to false if at least one bus offset does not
    equal_offsets = True
    i = 1
    last_bus = 0
    while i < len(busses) and equal_offsets:
        if busses[i] != 'x':
            if (time + i) % busses[i] > 0:
                equal_offsets = False
            else:
                last_bus = last_bus + 1
        i = i + 1
    # ended the loop with all busses having the same offsets : we did it !
    if equal_offsets:
        found = True
    else:
        if max_count < last_bus:
            max_count = last_bus
    if max_count > 0:
        # jump directly to next time the same number of busses are in the same position
        step = 1
        for s in numbered_busses[:max_count]:
            step = step * s

print('Part 2 : %d' % time)
