# puzzle prompt: https://adventofcode.com/2024/day/7

import sys
import time

sys.path.insert(0,"..")

from operator import add, mul

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 7
    
    _is_debugging = False

    CONCAT  = lambda self, x, y: int(f"{x}{y}")

    def GetEquations(self, input):
        equations = [equation.split(": ") for equation in input]

        equations = [(int(result), list(map(int, numbers.split()))) for result, numbers in equations]

        return equations
    
    #straightforward solution, try all combinations of operators between numbers
    def SolveEquation(self,result, numbers, operators):
        def calc(result, numbers, curr):
            if curr > result:
                return False
            match numbers:
                case []: # no more numbers, test the result
                    return curr == result
                case [arg, *rest]: # test the next number with all operators
                    return any(calc(result, rest, operator(curr, arg)) for operator in operators)

        return calc(result, numbers[1:], numbers[0]) 

    def pt1(self, input):
        self.debug(input)

        equations = self.GetEquations(input)

        res = sum(result for result, numbers in equations 
                  if self.SolveEquation(result, numbers, [add, mul]))

        return res

    def pt2(self, input):
        self.debug(input)

        equations = self.GetEquations(input)

        res = sum(result for result, numbers in equations 
                  if self.SolveEquation(result, numbers, [add, mul, self.CONCAT]))

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