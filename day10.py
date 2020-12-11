#!/usr/bin/env python3
import sys

# read file, strip \n
adapters = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        adapters.append(int(line.strip()))

highest = max(adapters) + 3

adapters.sort()
adapters.append(highest)

prev = 0
diffs = dict()
offsets = []
for a in adapters:
    diff = a - prev
    offsets.append(diff)
    if diff not in diffs:
        diffs[diff] = 1
    else:
        diffs[diff] = diffs[diff] + 1
    prev = a

print ('Part 1 : %d' % (diffs[1] * diffs[3]))

def arr(k, n):
    # A(n,k) = n! / (n - k)! = n * (n - 1) * (n - 2) * ... * (n - k + 1)
    res = 1
    for i in range(0, k):
        res = res * (n - i)

    return int(res)

# count how many combinations are still valid
# when removing 1 or 2 elements in a list of at least 2 sequential ones
def count_comb(offset):
    # number of combinations of 1 element in offset - 1
    # +
    # number of combinations of 2 elements in offset - 1

    # (offset - 1) because last one cannot be removed, or else next diff will > 3

    # C(n,k) = A(n,k) / k!

    arr1 = arr(1, offset - 1)      # / fact(1)
    arr2 = arr(2, offset - 1) / 2  # / fact(2)

    # add 1 because we also need to return unchanged list (no removal)
    return int(arr1 + arr2 + 1)

offset = 0
mul = 1
for o in offsets:
    if o == 1:
        offset = offset + 1
    else:
        if offset >= 2:
            mul = mul * count_comb(offset)
        offset = 0

print ('Part 2 : %d' % mul)
