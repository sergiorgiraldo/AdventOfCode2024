# puzzle prompt: https://adventofcode.com/2024/day/11

import sys
import time

sys.path.insert(0,"..")

from collections import Counter

from base.advent import *


class Solution(InputAsStringSolution):
    _year = 2024
    _day = 11
    
    _is_debugging = False

    def Blink(self, input):
        res = []
        stones = Counter([int(val) for val in input.split()])

        for i in range(75):
            for val, occurrences in list(stones.items()):
                if val == 0:                                #when 0 then 1
                    stones[1] += occurrences
                elif len(value := str(val)) % 2 == 0:       #when len is even, split
                    stones[int(value[:len(value)//2])] += occurrences
                    stones[int(value[len(value)//2:])] += occurrences
                else:
                    stones[val * 2024] += occurrences       #fallback, mul by 2024

                stones[val] -= occurrences

            if i in (24, 74): # magic numbers from the puzzle
                res.append(sum(stones.values()))

        return res
    
    def pt1(self, input):
        self.debug(input)

        res = self.Blink(input)[0]

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.Blink(input)[1]

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