# puzzle prompt: https://adventofcode.com/2024/day/13

import sys
import time

sys.path.insert(0,"..")

import re

import z3
from base.advent import *


class Solution(InputAsBlockSolution):
    _year = 2024
    _day = 13
    
    _is_debugging = False

    # Z3! this is learned day 24 in 2023
    def GetThePrize(self, input):
        res = [0, 0]

        regex = r"(\d+).*?(\d+)"

        for block in input:
            machine = "".join(block)

            (a_x,a_y), (b_x,b_y), (prize_x,prize_y) = [map(int, val) for val in re.findall(regex, machine)]

            for i, add in enumerate([0, 10_000_000_000_000]): #magic number from the puzzle
                solver = z3.Optimize()

                #variables
                a, b = z3.Int("a"), z3.Int("b")

                #constraints
                solver.add(prize_x + add == a * a_x + b * b_x)
                solver.add(prize_y + add == a * a_y + b * b_y)
                
                #equation
                solver.minimize(a * 3 + b) #token a costs 3, token b costs 1

                if solver.check() == z3.sat:
                    model = solver.model()
                    res[i] += model.eval(a).as_long() * 3 + model.eval(b).as_long()

        return res

    def pt1(self, input):
        self.debug(input)

        res = self.GetThePrize(input)[0]

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.GetThePrize(input)[1]

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