import fileinput
from collections import Counter, defaultdict

inputArr = [int(line) for line in fileinput.input()]

def partOne() -> int: 
    startingJoltage = 0
    jumps = []
    deviceJolts = max(inputArr) + 3
    print(f'Device joltage = {deviceJolts}')

    currAdaptor = 0
    while deviceJolts - currAdaptor > 3 :
        for i in range(currAdaptor + 1, currAdaptor + 4):
            print(f'looking for: {i}')
            if i in inputArr:
                jumps.append(i - currAdaptor)
                currAdaptor = i
                break

    jumps.append(deviceJolts - currAdaptor)
    counts = {i:jumps.count(i) for i in jumps}
    print(counts)
    print(counts[1] * counts[3])

def partTwo():
    deviceJolts = max(inputArr) + 3
    adapters = sorted(inputArr)
    
    # add 0 and device joltage
    adapters.insert(0, 0)
    adapters.append(deviceJolts)

    hashmap = dict()
    hashmap[0] = 1
    for i in range(len(adapters)):
        
        # try all options
        for j in range(1,4):
            try:
                hashmap[adapters[i] + j] += hashmap[adapters[i]]
            except KeyError:
                hashmap[adapters[i] + j] = hashmap[adapters[i]]
        
    print(hashmap[adapters[len(adapters)-1]])


# partOne()
partTwo()