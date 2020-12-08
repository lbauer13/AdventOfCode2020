#!/usr/bin/env python3
import sys,re

# read file, strip \n
rules = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        rules.append(line.strip())

colors = dict()
for rule in rules:
    m = re.search('(.*) bags contain (.*).', rule)
    color = m.group(1)
    cont  = m.group(2)
    colors[color] = dict()
    if cont != 'no other bags':
        for bags in cont.split(','):
            c = re.search('(\d+) (.*) bag', bags)
            colors[color][c.group(2)] = c.group(1)

def contains(outer, inner):
    result = False
    if colors[outer]:
        if inner in colors[outer].keys():
            return True
        for c in colors[outer].keys():
            if contains(c, inner):
                result = True

    return result

def contained(color):
    result = 0
    for c in colors[color].keys():
        result = result + int(colors[color][c]) + int(colors[color][c]) * contained(c)
    return result

count_1 = 0
for c in colors.keys():
    if contains(c, 'shiny gold'):
        count_1 = count_1 + 1

print ('Part 1 : %d' % count_1)
print ('Part 2 : %d' % contained('shiny gold'))
