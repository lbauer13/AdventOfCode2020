#!/usr/bin/env python3
import sys,re

# read file, strip \n
directions = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        m = re.search('(\w)(\d+)', line.rstrip())
        directions.append([m.group(1), int(m.group(2))])

#
turns = { 'R90': { 'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E' }, 'L90': { 'S': 'E', 'W': 'S', 'N': 'W', 'E': 'N' }, 'R180': { 'E': 'W', 'S': 'N', 'W': 'E', 'N': 'S' }, 'L180': { 'E': 'W', 'S': 'N', 'W': 'E', 'N': 'S' }, 'L270': { 'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E' }, 'R270': { 'S': 'E', 'W': 'S', 'N': 'W', 'E': 'N' } }

# latitude / longitude / facing direction
facing = 'E'
lt = 0
lg = 0

for d in directions:
    if d[0] == 'F':
        if (facing == 'E'):
            lg = lg + d[1]
        if (facing == 'W'):
            lg = lg - d[1]
        if (facing == 'N'):
            lt = lt - d[1]
        if (facing == 'S'):
            lt = lt + d[1]
    if d[0] == 'N':
        lt = lt - d[1]
    if d[0] == 'S':
        lt = lt + d[1]
    if d[0] == 'E':
        lg = lg + d[1]
    if d[0] == 'W':
        lg = lg - d[1]
    if d[0] == 'R' or d[0] == 'L':
        facing = turns[d[0]+str(d[1])][facing]

print ('Part 1 : %d' % (abs(lt) + abs(lg)))

# latitude / longitude / waypoint
lt = 0
lg = 0
wplg = 10
wplt = -1

def rotate(lg, lt, d, angle):
    if d + str(angle) in ['R90', 'L270']:
        nlt = lg
        nlg = 0 - lt
    if d + str(angle) in ['L90', 'R270']:
        nlt =  0 - lg
        nlg =  lt
    if d + str(angle) in ['L180', 'R180']:
        nlt =  0 - lt
        nlg =  0 - lg
    return [nlg, nlt]

for d in directions:
    if d[0] == 'F':
        lg = lg + d[1] * wplg
        lt = lt + d[1] * wplt
    if d[0] == 'N':
        wplt = wplt - d[1]
    if d[0] == 'S':
        wplt = wplt + d[1]
    if d[0] == 'E':
        wplg = wplg + d[1]
    if d[0] == 'W':
        wplg = wplg - d[1]
    if d[0] == 'R' or d[0] == 'L':
        newwp = rotate(wplg, wplt, d[0], d[1])
        wplg = newwp[0]
        wplt = newwp[1]

print ('Part 2 : %d' % (abs(lt) + abs(lg)))
