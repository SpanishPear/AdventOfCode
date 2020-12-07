import fileinput
from functools import reduce
import sys

def partOne():
    partOne = sum([len(list(dict.fromkeys(list(item.replace('\n',''))))) for item in sys.stdin.read().split('\n\n')])
    print(partOne)

def partTwo():
    partTwo = sum([len(set.intersection(*[set(list(item)) for item in item.split()])) for item in sys.stdin.read().split('\n\n')]) 
print(partTwo)