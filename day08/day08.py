import fileinput
from functools import reduce
import copy

inputArr = [line.strip() for line in fileinput.input()]

# one instruction per lione
# acc [-+]<int>  - increases global accumulator by argument. global acc starts at 0 
# jmp [-+]<int>  - jump to instruction relative to itself. jmp +2 skips one instruction, executes the next one. NOT jump over 2. 
# nop [-+]<int>  - does nothing

def partOne(instructions):
    programCounter = 0
    accumulator = 0
    visitedInstructions = set()

    while programCounter < len(instructions) and programCounter not in visitedInstructions:
        item = instructions[programCounter]
        visitedInstructions.add(programCounter)
        instr, value = item.split()
        value = int(value)
        print('\t\t', instr, value)
        if instr == "acc":
            accumulator += value
            programCounter += 1
        elif instr == "nop":
            programCounter += 1
        elif instr == "jmp":
            programCounter += value

    print(f'\tfinishing at {programCounter} ')
    return (programCounter == len(instructions), accumulator)


def partTwo():
    for i, item in enumerate(inputArr):
        instr, value = item.split()

        if instr in ("nop", "jmp"):
            newInstrSet = copy.deepcopy(inputArr)
            newInstr = "jmp" if instr == "nop" else "nop"
            newInstrSet[i] = f'{newInstr} {value}' 
            print('\n',newInstrSet)
            
            finished, acc = partOne(newInstrSet)
            if finished: return acc

print(partOne(inputArr)[1])
print(partTwo())