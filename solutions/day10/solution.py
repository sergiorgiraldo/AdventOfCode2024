# puzzle prompt: https://adventofcode.com/2024/day/10

import sys
import time

sys.path.insert(0,"..")

from collections import defaultdict

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 10
    
    _is_debugging = False

    # complex numbers, same idea from day 04
    def GetMatrix(input):
        m = defaultdict(int)

        for i, line in enumerate(input):
            for j, c in enumerate(line):
                m[i + 1j * j] = int(c)  
        
        return m
    
    def Hike(self, coords, current, unique, some=0):
        if coords[current] == 9: 
            unique.add(current)
            return 1
        
        for offset in [1, 1j, -1, -1j]: #walk 1 step in each direction
            if coords.get(current + offset) == coords[current] + 1:
                some += self.Hike(coords, current + offset, unique)

        return some

    def FindTrailheads(self, input):
        matrix = self.GetMatrix(input)

        paths, ratings = {c: set() for c in matrix}, 0
        for c in matrix:
            if matrix[c] == 0:
                ratings += self.Hike(matrix, c, paths[c])

        return sum(map(len, paths.values())), ratings

    def pt1(self, input):
        self.debug(input)

        res, _ = self.FindTrailheads(input)

        return res

    def pt2(self, input):
        self.debug(input)

        _, res = self.FindTrailheads(input)

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