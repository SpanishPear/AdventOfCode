import fileinput

TARGET = 2020
inputArr = []
for line in fileinput.input():
    item = int(line)
    inputArr.append(item)

def partOne(target):

    # the default implementation (CPython) of a set is a hashtable with optimisations
    # therefore average O(1) lookup and average O(1) insertion
    s = set()
    # print("attempting to find the target: ", target)
    for line in inputArr:
        item = int(line)
        complement = abs(item - target)
        if complement in s and complement + item == target :
            # print("PARTS:", item, complement)
            return (item, complement)
            # print('ANSWER', abs(item * (item - target))) 
        s.add(item)
    
    return False

print(partOne(TARGET)[0] * partOne(TARGET)[1])

twoParts = set()
for i in range(len(inputArr)):
    s = set()
    curr_sum = TARGET - inputArr[i]

    # and now we do part one with currsum as the target
    # print("looking for", curr_sum)
    items = partOne(curr_sum)
    if (items != False):
        a, b = items
        print("pieces: ", a , b, inputArr[i])
        print("sum: ", a + b + inputArr[i])
        print("product: ", a * b * inputArr[i])
        break