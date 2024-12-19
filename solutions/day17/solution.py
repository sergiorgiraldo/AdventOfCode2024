# puzzle prompt: https://adventofcode.com/2024/day/17

import sys
import time

sys.path.insert(0,"..")

from base.advent import *
import re

class Solution(InputAsBlockSolution):
    _year = 2024
    _day = 17
    
    _is_debugging = False

    def Setup(self, input):
        regs, program = input[0], input[1]
        self.registers = {}
        
        regex = r"(A|B|C):\ (\d+)"
        for reg in regs:
            match = re.search(regex, reg)
            self.registers[match.group(1)] = int(match.group(2))
        
        self.program = [int(op) for op in program[0].split(": ")[1].split(",")]

    #pass registers as parameter for part 2, to simulate the program and keep regs B and c zeroed
    def Run(self, registers, part = 1):
        def Combo(operand):
            if operand < 4:
                return operand
            if operand == 4:
                return registers["A"]
            if operand == 5:
                return registers["B"]
            if operand == 6:
                return registers["C"]
            else:
                raise("combo 7 is reserved")

        length = len(self.program)
        ip = 0
        output = []

        while ip < length - 1:
            to_jump = True
            
            operator, operand = self.program[ip:ip+2]
            
            if operator == 0: #adv
                registers["A"] = registers["A"] // (2**Combo(operand))
            elif operator == 1: #bxl
                registers["B"] = registers["B"] ^ operand
            elif operator == 2: #bst
                registers["B"] = Combo(operand) % 8
            elif operator == 3: #jnz
                if registers["A"] != 0:
                    ip = operand
                    to_jump = False
            elif operator == 4: #bxc
                registers["B"] = registers["B"] ^ registers["C"]
            elif operator == 5: #out
                val = Combo(operand) % 8
                # print("D:",register, ">>", val)
                if part == 2:
                    return val
                output.append(val)
            elif operator == 6: #bdv
                registers["B"] = registers["A"] // (2**Combo(operand))
            elif operator == 7: #cdv
                registers["C"] = registers["A"] // 2**Combo(operand)

            if to_jump:
                ip += 2
            # print("D:cmd",cmd, ":", register)
        res = ",".join(map(str, output))
        
        return res

    # I solved part 3 brute-force to get the star. Then I knew that I could decompile the program
    # and made it run the math operations. See `alternative.py`
    def Replicate(self):
        offset = len(self.program)-1
        current_As = [0]

        while offset >= 0:
            # print(current_As)
            next_As = []
            expected = self.program[offset]
            
            # check decompile, program runs in batches of 8 commands
            for register_A in current_As:
                new_register_A = register_A * 8

                for i in range(8):
                    current_A = new_register_A + i
                    self.registers["A"] = current_A
                    output = self.Run(self.registers, 2)
                    if output == expected:
                        next_As.append(current_A)
                        #print(expected, current_A, next_As)

            offset -= 1
            current_As = [item for item in next_As]
        return min(current_As)
    
    def pt1(self, input):
        self.debug(input)

        self.Setup(input)

        res = self.Run(self.registers)

        return res

    def pt2(self, input):
        self.debug(input)

        self.Setup(input)

        res = self.Replicate()

        return res
        
    def part_1(self):
        start_time = time.time()

        res = self.pt1(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.pt2(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()