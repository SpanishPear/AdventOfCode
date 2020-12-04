from collections import defaultdict
import re

def partOne():
    with open('input.txt') as f:
        contents = f.read()

    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    valid = 0
    for item in contents.split('\n\n'):
        
        found = {k:False for k in keys}
        for key in keys:
            if key in item:
                found[key] = True

        if all(found.values()):
            valid += 1

        
    print(valid)

def partTwo():
    with open('input.txt') as f:
        contents = f.read()
    
    patterns = [r'byr:(\d{4})(?: |\n)', r'iyr:(\d{4})(?: |\n)', r'eyr:(\d{4})(?: |\n)', r'hgt:(\d+)(cm|in){1}(?: |\n)', r'hcl:(#[0-9a-f]{6})(?: |\n)', r'ecl:(amb|blu|brn|gry|grn|hzl|oth){1}(?: |\n)', r'pid:(\d{9})(?: |\n)']

    valid = 0
    
    for item in contents.split('\n\n'):
        item += ' '
        found = []
        error = False

        # print('=====\n',item)
        
        for i, pattern in enumerate(patterns):
            match = re.search(pattern, item)
            # print(match)
            # not required format - so go to next passport, skip validation
            if (match == None): 
                error = True
                break

            found.append(match.groups())
        
        if (error): 
            continue
        
        print(found)

        # BYR check
        if int(found[0][0]) < 1920 or int(found[0][0]) > 2002:
            print('byr false')
            continue
        
        # IYR check
        if int(found[1][0]) < 2010 or int(found[1][0]) > 2020:
            print('iyr false')
            continue
        
        # EYR check: 
        if int(found[2][0]) < 2020 or int(found[2][0]) > 2030:
            print('eyr false')
            continue
        
        # HGT check
        if  (found[3][1]) == 'in':
            if int(found[3][0]) < 59 or int(found[3][0]) > 76:
                print('HGT false')
                continue
        elif found[3][1] == 'cm':
            if int(found[3][0]) < 150 or int(found[3][0]) > 193:
                print('HGT cm false')
                continue
        
        # HCL check -- not needed just regex

        # ECL check -- not needed, just regex

        # PID check -- not needed, just regex
        
        valid += 1

    print(valid)


partTwo()
