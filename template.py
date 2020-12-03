import fileinput

TARGET = 2020
inputArr = []
for line in fileinput.input():
    item = int(line)
    inputArr.append(item)