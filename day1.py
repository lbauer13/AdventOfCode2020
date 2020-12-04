#!/usr/bin/env python3
import sys

def to_int(string):
    return int(string)

# read file, convert strings to integers
inputs = []
with open(sys.argv[1], 'r') as f:
    inputs = list(map(to_int, f.readlines()))

input_sum = 0
input_mul = 0
x = 0
y = 1

# how ugly !
# sure python can do better with map() and better data structures...
# will try next time :)

while x < len(inputs)-1 and input_sum != 2020:
    while y < len(inputs) and input_sum != 2020:
        input_sum = inputs[x] + inputs[y]
        input_mul = inputs[x] * inputs[y]
        y = y + 1
    x = x + 1
    y = x + 1

print('Part 1 : %d' % input_mul)

# no comment (see above)

input_sum = 0
input_mul = 0
x = 0
y = 1
z = 2
while x < len(inputs)-1 and input_sum != 2020:
    while y < len(inputs) and input_sum != 2020:
        while z < len(inputs) and input_sum != 2020:
            input_sum = inputs[x] + inputs[y] + inputs[z]
            input_mul = inputs[x] * inputs[y] * inputs[z]
            z = z + 1
        y = y + 1
        z = y + 1
    x = x + 1
    y = x + 1
    z = y + 1

print('Part 2 : %d' % input_mul)
