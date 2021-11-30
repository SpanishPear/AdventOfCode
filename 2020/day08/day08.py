import fileinput
from functools import reduce
import copy

inputArr = [line.strip() for line in fileinput.input()]

# one instruction per lione
# acc [-+]<int>  - increases global accumulator by argument. global acc starts at 0 
# jmp [-+]<int>  - jump to instruction relative to itself. jmp +2 skips one instruction, executes the next one. NOT jump over 2. 
# nop [-+]<int>  - does nothing

class cpu():
    def __init__(self, instructions):
        self.PC = 0
        self.acc = 0
        self.visited = []
        self.terminated = False
        self.instructions = instructions

    def run(self):
        while self.PC < len(self.instructions) and self.PC not in self.visited:
            item = self.instructions[self.PC]
            self.visited.append(self.PC)
            instr, value = item.split()
            value = int(value)
            if instr == "acc":
                self.acc += value
                self.PC += 1
            elif instr == "nop":
                self.PC += 1
            elif instr == "jmp":
                self.PC += value

        # print(self.PC, len(self.instructions))
        self.terminated = self.PC == len(self.instructions)

    def status(self):
        return (self.terminated, self.acc)




def partOne(instructions):
    myCpu = cpu(instructions)
    myCpu.run()
    print(myCpu.acc)

def partTwo():
    for i, item in enumerate(inputArr):
        instr, value = item.split()

        if instr in ("nop", "jmp"):
            newInstrSet = copy.deepcopy(inputArr)
            newInstr = "jmp" if instr == "nop" else "nop"
            newInstrSet[i] = f'{newInstr} {value}' 
            
            myCpu = cpu(newInstrSet)
            myCpu.run()
            if myCpu.terminated: return myCpu.acc

partOne(inputArr)
print(partTwo())