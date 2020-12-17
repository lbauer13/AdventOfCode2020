#!/usr/bin/env python3
import sys,re

fields = dict()
mine = []
nearby = []
with open(sys.argv[1], 'r') as f:
    l = f.readline().rstrip()
    while l:
        g = re.search('(.*): (.*)-(.*) or (.*)-(.*)', l)
        if g:
            fields[g.group(1)] = [ range(int(g.group(2)), int(g.group(3))+1), range(int(g.group(4)), int(g.group(5))+1) ]
        l = f.readline().rstrip()
    l = f.readline().rstrip()
    # your ticket
    while l:
        if l != 'your ticket:':
            mine = [ int(i) for i in l.split(',') ]
        l = f.readline().rstrip()
    l = f.readline().rstrip()
    # nearby tickets
    while l:
        if l != 'nearby tickets:':
            nearby.append([ int(i) for i in l.split(',') ])
        l = f.readline().rstrip()

invalid = 0
valid_tickets = []
for t in nearby:
    ticket_is_valid = True
    for i in t:
        has_valid = False
        for j,(field,ranges) in enumerate(fields.items()):
            for r in ranges:
                if i in r:
                    has_valid = True
        if not has_valid:
            invalid = invalid + i
            ticket_is_valid = False
    if ticket_is_valid:
        valid_tickets.append(t)

print ('Part 1 : %d' % invalid)

fields_valid_pos = dict()
for f in fields.keys():
    fields_valid_pos[f] = []
    #for i in range(0, len(mine)):
    #    fields_valid_pos[f].append(i)

for j,(field,ranges) in enumerate(fields.items()):
    for i in range(0, len(valid_tickets[0])):
        all_valid = True
        for t in valid_tickets:
            in_range = False
            for r in ranges:
                if t[i] in r:
                    in_range = True
            if not in_range:
                all_valid = False
        if all_valid and i not in fields_valid_pos[field]:
            fields_valid_pos[field].append(i)

# for each range, find the index that is only valid for this range
reserved_idx = []
done = False
while not done:
    done = True
    for j,(field,rg) in enumerate(fields_valid_pos.items()):
        if len(rg) == 1:
            if rg[0] not in reserved_idx:
                reserved_idx.append(rg[0])
        else:
            done = False
        # this index is only valid for current field, remove from others
        for r in reserved_idx:
            if r in rg and len(rg) > 1:
                rg.remove(r)

# find fields starting with 'departure'
part2 = 1
for i,(field,rg) in enumerate(fields_valid_pos.items()):
    if re.search('^departure', field):
        part2 = part2 * mine[rg[0]]

print ('Part 2 : %d' % part2)
