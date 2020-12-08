#!/usr/bin/env python3
import sys,re

# read file, strip \n
instructions = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        i = re.search('(.*) ([+-].*)', line.rstrip())
        inst = dict()
        inst['instruction'] = i.group(1)
        inst['offset']      = int(i.group(2))
        instructions.append(inst)

def play(instructions):
    ptr    = 0
    acc  = 0
    done = list()

    while ptr not in (done) and ptr < len(instructions):
        done.append(ptr)

        (inst, off) = instructions[ptr]['instruction'], instructions[ptr]['offset']
        if inst == 'nop':
            ptr = ptr + 1
        if inst == 'acc':
            ptr = ptr + 1
            acc = acc + off
        if inst == 'jmp':
            ptr = ptr + off

    if (ptr >= len(instructions)):
        return (True, acc)
    else:
        return(False, acc)

print ('Part 1 : %d' % play(instructions)[1])

i = 0
stops = False
while not stops :
    if (instructions[i]['instruction'] == 'jmp'):
        instructions[i]['instruction'] = 'nop'
        (stops, acc) = play(instructions)
        instructions[i]['instruction'] = 'jmp'
    if (instructions[i]['instruction'] == 'nop'):
        instructions[i]['instruction'] = 'jmp'
        (stops, acc) = play(instructions)
        instructions[i]['instruction'] = 'nop'
    i = i + 1

print ('Part 2 : %d' % acc)
