# puzzle prompt: https://adventofcode.com/2024/day/22

import time
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 22
    
    _is_debugging = True

    def pt1(self, input):
        x = [1,2]
        self.debug(x)

        return ""

    def pt2(self, input):
        self.debug(input)

        return ""
        
    def part_1(self):
        start_time = time.time()

        res = self.pt1(self.input)

        end_time = time.time()

        # self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.pt2(self.input)

        end_time = time.time()

        # self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    # solution.part_2()