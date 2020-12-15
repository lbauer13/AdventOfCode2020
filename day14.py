#!/usr/bin/env python3
import sys, re

# read file, strip \n
inputs = []
with open(sys.argv[1], 'r') as f:
    inputs = [line.strip() for line in f];

mem = dict()

for line in inputs:
    g = re.search('mask = (.*)', line)
    if g:
        bitmask = list(g.group(1))
        bitmask.reverse()
    g = re.search('mem\[(.*)\] = (.*)', line)
    if g:
        val    = int(g.group(2))
        memval = 0
        for bit in range(0, len(bitmask)):
            if bitmask[bit] == 'X':
                memval = memval + (val & 2**bit)
            if bitmask[bit] == '1':
                memval = memval + 2**bit
        mem[g.group(1)] = memval

print('Day 1 : %d' % sum(mem.values()))

mem = dict()

def get_mem_addresses(memmask):
    addresses = []
    if 'X' in memmask:
        idx = memmask.index('X')
        newmask = memmask.copy()
        newmask[idx] = 0
        addresses = addresses + get_mem_addresses(newmask)
        newmask[idx] = 1
        addresses = addresses + get_mem_addresses(newmask)
    else:
        a = 0
        for i in range(0, len(memmask)):
            if memmask[i] == 1:
                a = a + 2**i
        addresses = [ a ]

    # not needed, for debug only
    # addresses.sort()

    return addresses

for line in inputs:
    g = re.search('mask = (.*)', line)
    if g:
        bitmask = list(g.group(1))
        bitmask.reverse()
    g = re.search('mem\[(.*)\] = (.*)', line)
    if g:
        memmask = []
        val     = int(g.group(2))
        addr    = int(g.group(1))
        for bit in range(0, len(bitmask)):
            if bitmask[bit] == 'X':
                memmask.append(bitmask[bit])
            if bitmask[bit] == '1':
                memmask.append(int(bitmask[bit]))
            if bitmask[bit] == '0':
                memmask.append(min(1, addr & 2**bit))
        # write at all given addresses
        for a in get_mem_addresses(memmask):
            mem[a] = val

print ('Part 2 : %d' % sum(mem.values()))
