#!/usr/bin/python3
import sys, re

# read file, strip \n
pports = []
data = {}
with open(sys.argv[1], 'r') as f:
    for line in f:
        if line.rstrip() == '':
            pports.append(data)
            data = {}
        else:
            for val in line.rstrip().split(' '):
                (k,v) = val.split(':')
                data[k] = v

mandatory = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

count_valid = 0
for pp in pports:
    common_keys = (list(set(pp.keys()) & set(mandatory)))
    if len(common_keys) == 7:
        count_valid = count_valid + 1

print ('Part 1 : %d' % count_valid);

def check_year(str, min, max):
    return str and int(str) in range(min, max + 1)

def check_hgt(str):
    hgt = re.match('(\d+)(\w+)', str)
    if hgt:
        if hgt.group(2) == 'cm' and int(hgt.group(1)) in range(150, 194):
            return True
        if hgt.group(2) == 'in' and int(hgt.group(1)) in range(59, 77):
            return True
        return False
    else:
        return False

def check_hcl(str):
    return re.match('#[0-9a-f]{6}', str)

def check_ecl(str):
    return str in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_pid(str):
    return re.match('\d+', str) and len(str) == 9

count_valid = 0
for pp in pports:
    common_keys = (list(set(pp.keys()) & set(mandatory)))
    if len(common_keys) == 7:
        is_valid = True

        if not check_year(pp['byr'], 1920, 2002):
            is_valid = False
        if not check_year(pp['iyr'], 2010, 2020):
            is_valid = False
        if not check_year(pp['eyr'], 2020, 2030):
            is_valid = False

        if not check_hgt(pp['hgt']):
            is_valid = False

        if not check_hcl(pp['hcl']):
            is_valid = False
        if not check_ecl(pp['ecl']):
            is_valid = False

        if not check_pid(pp['pid']):
            is_valid = False

        if is_valid:
            count_valid = count_valid + 1

print ('Part 2 : %d' % count_valid);
