# puzzle prompt: https://adventofcode.com/2024/day/17

import sys
import time

sys.path.insert(0,"..")
import copy

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 17
    
    _is_debugging = False

    def Setup(self, input):
        self.original_register_list = []

        for line in input:
            if line.startswith("Reg"):
                reg = line.split(": ")[1]
                self.original_register_list.append(int(reg))
            elif line.startswith("Pro"):
                program = line.split(": ")[1]
                self.original_program = tuple(map(int, program.split(",")))

        self.original_register_tuple = tuple(self.original_register_list)

    def Run(self, register_A, registers, part = 1):
        length = len(self.original_program)
        register = {}
        for v, r in enumerate(["A","B","C"]):
            register[r] = registers[v]
        cmd = 0
        output = []
        register["A"] = register_A

        def Combo(operand):
            if operand < 4:
                return operand
            if operand == 4:
                return register["A"]
            if operand == 5:
                return register["B"]
            if operand == 6:
                return register["C"]
            else:
                print("7 combo detected")

        while cmd < length - 1:
            to_jump = True
            
            operator, operand = self.original_program[cmd:cmd+2]
            
            if operator == 0: #adv
                register["A"] = register["A"] // (2**Combo(operand))
            elif operator == 1: #bxl
                register["B"] = register["B"] ^ operand
            elif operator == 2: #bst
                register["B"] = Combo(operand) % 8
            elif operator == 3: #jnz
                if register["A"] != 0:
                    cmd = operand
                    to_jump = False
            elif operator == 4: #bxc
                register["B"] = register["B"] ^ register["C"]
            elif operator == 5: #out
                val = Combo(operand) % 8
                # self.debug("D:",register, ">>", val)
                if part == 2:
                    return val
                output.append(val)
            elif operator == 6: #bdv
                register["B"] = register["A"] // (2**Combo(operand))
            elif operator == 7: #cdv
                register["C"] = register["A"] // 2**Combo(operand)

            if to_jump:
                cmd += 2

            # self.debug("D:cmd",cmd, ":", register)
        res = ",".join(map(str, output))
        
        return res

    def Replicate(self):
        offset = len(self.original_program)-1
        current_As = [0]

        while offset >= 0:
            next_As = []
            expected = self.original_program[offset]
            
            for register_A in current_As:
                new_register_A = register_A * 8

                # check decompile, program runs in batches of 8 commands
                for y in range(8):
                    current_A = new_register_A + y
                    output = self.Run(current_A, self.original_register_tuple, 2)
                    if output == expected:
                        next_As.append(current_A)

            offset -= 1
            current_As = copy.deepcopy(next_As)

        return min(current_As)
    
    def pt1(self, input):
        self.debug(input)

        self.Setup(input)

        res = self.Run(self.original_register_tuple[0], self.original_register_tuple)

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