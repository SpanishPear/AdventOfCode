import fileinput
import re

def partTwo():
    numValid = 0
    pattern = r'(\d{1,2})-(\d{1,2}) ([a-zA-Z]): (\w+)'

    for line in fileinput.input():
        match = re.match(pattern, line)
        pos1, pos2, char, password = match.groups()
        count = 0

        letterOne = password[int(pos1) - 1]
        letterTwo = password[int(pos2) - 1] 
        if ( (letterOne == char or letterTwo == char) and (letterOne != letterTwo) ): 
            numValid += 1

    return numValid


def partOne():
    numValid = 0
    pattern = r'(\d{1,2})-(\d{1,2}) ([a-zA-Z]): (\w+)'

    for line in fileinput.input():
        match = re.match(pattern, line)
        minNum, maxNum, char, password = match.groups()
        count = 0
        for letter in password:
            if (char == letter):
                count += 1
        
        if ( int(minNum) <= count <= int(maxNum)):
            numValid  += 1


    return numValid


print(partTwo())