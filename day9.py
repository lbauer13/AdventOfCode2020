#!/usr/bin/env python3
import sys,re

# read file, strip \n
numbers = []
length = int(sys.argv[2])
with open(sys.argv[1], 'r') as f:
    for line in f:
        numbers.append(int(line.strip()))

def find_invalid(numbers, length):
    found_invalid = False
    i = length
    while not found_invalid and i <= len(numbers):
        previous = numbers[i-length:i]
        is_valid = False
        for n1 in range(0, len(previous) - 1):
            for n2 in range(n1 + 1, len(previous)):
                if numbers[i] == previous[n1] + previous[n2]:
                    is_valid = True
        if not is_valid:
            found_invalid = True
        i = i + 1
    return numbers[i-1]

invalid = find_invalid(numbers, length)
print('Part 1 : %d' % invalid)

found = False
i = 0
while not found and i < len(numbers)-1:
    j = i + 1
    mysum = 0
    while not found and j < len(numbers) and mysum < invalid:
        mysum = sum(numbers[i:j+1])
        found = (mysum == invalid)
        j = j + 1
    if found:
        print('Part 2 : %d' % (min(numbers[i:j]) + max(numbers[i:j])))
    i = i + 1
