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
        self.OriginalRegisterList = []
        for t in input:
            Line = t.strip()
            if Line.startswith("Reg"):
                _, _, A = Line.split()
                self.OriginalRegisterList.append(int(A))
            elif Line.startswith("Pro"):
                _, A = Line.split()
                self.Originalprogram = tuple(map(int, A.split(",")))
                self.CompareString = A
        self.OriginalRegisterT = tuple(self.OriginalRegisterList)

    def Program(self, RegA, RegisterTuple, Part):
        ProgramLength = len(self.Originalprogram)
        Register = {}
        for v, r in enumerate(["A","B","C"]):
            Register[r] = RegisterTuple[v]
        Pointer = 0
        OutputList = []
        Register["A"] = RegA

        def Combo(Operand):
            if Operand < 4:
                return Operand
            if Operand == 4:
                return Register["A"]
            if Operand == 5:
                return Register["B"]
            if Operand == 6:
                return Register["C"]
            else:
                print("7 combo detected")

        while Pointer < ProgramLength-1:
            PointerJump = True
            Operator, Operand = self.Originalprogram[Pointer:Pointer+2]
            if Operator == 0: #adv
                Numerator = Register["A"]
                Denom = 2**Combo(Operand)
                Register["A"] = Numerator // Denom
            elif Operator == 1: #bxl
                B = Register["B"]
                Register["B"] = B ^ Operand
            elif Operator == 2: #bst
                Register["B"] = Combo(Operand) % 8
            elif Operator == 3: #jnz
                if Register["A"] != 0:
                    Pointer = Operand
                    PointerJump = False
            elif Operator == 4: #bxc
                B, C = Register["B"], Register["C"]
                Register["B"] = B ^ C
            elif Operator == 5: #out
                Output = Combo(Operand) % 8
                if Part == 2:
                    return Output, Register["A"]
                OutputList.append(Output)

            elif Operator == 6: #bdv
                Numerator = Register["A"]
                Denom = 2**Combo(Operand)
                Register["B"] = Numerator // Denom
            elif Operator == 7: #cdv
                Numerator = Register["A"]
                Denom = 2**Combo(Operand)
                Register["C"] = Numerator // Denom

            if PointerJump:
                Pointer += 2

        OutputString = ""
        for t in OutputList:
            OutputString += str(t)
            OutputString += ","
        OutputString = OutputString[:-1]
        if Part == 1:
            return OutputString
        else:
            return True, OutputString

    def Replicate(self):
        Place = len(self.Originalprogram)-1
        CurrentRegAs = [0]

        while Place >= 0:
            NextRegAs = []
            ExpectedOutput = self.Originalprogram[Place]
            #print(ExpectedOutput, Place)
            for RA in CurrentRegAs:
                NewRA = RA*8
                for y in range(8):
                    CRA = NewRA + y
                    NewOutput, PassedA = self.Program(CRA, self.OriginalRegisterT, 2)
                    #print(CRA, NewOutput, NewOutput==ExpectedOutput, PassedA)
                    if NewOutput == ExpectedOutput:
                        NextRegAs.append(CRA)

            Place -= 1
            CurrentRegAs = copy.deepcopy(NextRegAs)

        return min(CurrentRegAs)
    
    def pt1(self, input):
        self.debug(input)

        self.Setup(input)

        res = self.Program(self.OriginalRegisterT[0], self.OriginalRegisterT, 1)

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