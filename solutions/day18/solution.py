# puzzle prompt: https://adventofcode.com/2024/day/18

import sys
import time

sys.path.insert(0,"..")

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 18
    
    _is_debugging = False

    def setup(self, input, test = False):
        if test:
            offset = 12
            start = 0
            end = 6 + 6j
        else:
            offset = 1024
            start = 0
            end = 70 + 70j

        fallen_bytes = set()

        for i in range(offset):
            x,y = input[i].split(",")
            fallen_bytes.add((int(x) + int(y) * 1j))

        return start, end, fallen_bytes
    
    def FindShortestPath2Exit(self, input):
        start, end, fallen_bytes = self.setup(input)

        queue = [(start, 0)]
        visited = set()

        while queue:
            pos, steps = queue.pop(0)
            if pos == end:
                return steps
            
            if pos in visited:
                continue
            
            visited.add(pos)

            for move in [1, -1, 1j, -1j]:
                new_pos = pos + move
                if new_pos in fallen_bytes:
                    continue
                if new_pos.real < 0 or new_pos.imag < 0:
                    continue
                if new_pos.real > end.real or new_pos.imag > end.imag:
                    continue
                queue.append((new_pos, steps + 1))
        return -1

    def GetBadByte(self, input):
        start, end, fallen_bytes = self.setup(input)

        for i in range(1024, len(input)):
            x,y = input[i].split(",")
            fallen_bytes.add((int(x) + int(y) * 1j))
            if self.FindShortestPath2Exit(start, end, fallen_bytes) == -1:
                res = input[i]
                break

        return res
    
    def pt1(self, input):
        self.debug(input)

        res = self.FindShortestPath2Exit(input)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.GetBadByte(input)

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