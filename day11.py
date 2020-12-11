#!/usr/bin/env python3
import sys, copy

# read file, strip \n
room = []
with open(sys.argv[1], 'r') as f:
    first_line = []
    for line in f:
        # add an empty border to room to avoid out of bound coordinates
        seats = ['.'] + list(line.rstrip()) + ['.']
        if len(room) == 0:
            first_line = list('.' * len(seats))
            room = [first_line]
        room.append(seats)
    room.append(first_line)


def print_map(room):
    for y in range(0, len(room)):
        print (' '.join(room[y]))
    print ('')

def count_next(room, x, y):
    count = 0
    string = room[y-1][x-1] + room[y-1][x] + room[y-1][x+1] + "\n"
    string = string + room[y][x-1] + '?' + room[y][x+1] + "\n"
    string = string + room[y+1][x-1] + room[y+1][x] + room[y+1][x+1] + "\n"

    for char in string:
        if char == '#':
            count = count + 1
    return (count)

def count_visible(room, x, y):
    # all 8 directions : order x, y
    directions = [[-1,-1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    count = 0
    for d in directions:
        first_seat = '.'
        # (re)start from current seat
        nx = x
        ny = y
        while ny > 0 and ny < len(room) and nx > 0 and nx < len(room[ny]) and first_seat == '.':
            nx = nx + d[0]
            ny = ny + d[1]
            if ny > 0 and ny < len(room) and nx > 0 and nx < len(room[ny]):
                first_seat = room[ny][nx]
                if first_seat == '#':
                    count = count + 1
                    break
    return count

def process_map(room, min_seats, method):
    new_room = copy.deepcopy(room)
    for y in range(1, len(room)-1):
        for x in range(1, len(room[y])-1):
            # function passed as argument ; different for part 1 and part 2
            nc = method(room, x, y)

            if room[y][x] == 'L' and nc == 0:
                new_room[y][x] = '#'
            if room[y][x] == '#' and nc >= min_seats:
                new_room[y][x] = 'L'
    return new_room

def compare_rooms(r1, r2):
    for y in range(0, len(r1)):
        for x in range(0, len(r1[y])):
            if r1[y][x] != r2[y][x]:
                return False
    return True

def count_seated(room):
    count = 0
    for y in range(0, len(room)):
        for x in range(0, len(room[y])):
            if room[y][x] == '#':
                count = count + 1
    return count

# copy initial input for round 2
initial_room = copy.deepcopy(room)

nr = room
while True:
    nr = process_map(room, 4, count_next)
    if compare_rooms(nr, room):
        break
    room = nr

print('Part 1 : %d' % count_seated(nr))

room = initial_room
while True:
    nr = process_map(room, 5, count_visible)
    if compare_rooms(nr, room):
        break
    room = nr

print('Part 2 : %d' % count_seated(nr))
