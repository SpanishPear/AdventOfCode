import fileinput
LENGTH = 25
inputArr = [int(line) for line in fileinput.input()]

def twoSum(target: int, numbers: list):    

    # the default implementation (CPython) of a set is a hashtable with optimisations
    # therefore average O(1) lookup and average O(1) insertion
    s = set()
    # print("attempting to find the target: ", target)
    for line in numbers:
        item = int(line)
        complement = abs(item - target)
        if complement in s and complement + item == target :
            # print("PARTS:", item, complement)
            return True
            # print('ANSWER', abs(item * (item - target))) 
        s.add(item)
    
    return False

def partOne() -> int:
    i = LENGTH
    offset = 0
    while i < len(inputArr):
        start_index = i - LENGTH 
        end_index = i - 1 
        result = twoSum(inputArr[i], inputArr[start_index: end_index + 1])
        if not result: 
            print(f'{inputArr[i]}: {result}')
            return inputArr[i]

        offset += 1
        i = LENGTH + offset

def partTwo() -> int:
    i = 0
    members = []
    last_segment_index = 0
    target = partOne()
    while i < len(inputArr):
        members.append(inputArr[i])
        # print(members)
        if sum(members) == target:
            return sum([min(members), max(members)])
        elif sum(members) > target:
            last_segment_index += 1
            members = []
            i = last_segment_index
        else: 
            i += 1


partOne()
print(partTwo() )