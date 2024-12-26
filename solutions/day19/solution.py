# puzzle prompt: https://adventofcode.com/2024/day/19

import sys
import time

sys.path.insert(0, "..")

from itertools import product

from base.advent import *


class Solution(InputAsBlockSolution):
    _year = 2024
    _day = 19

    _is_debugging = False

    def DesignTowels(self, input):
        patterns, designs = input[0][0], input[1]
        patterns = patterns.split(", ")

        towels = [self.FindArrangements(design, patterns) for design in designs]

        return sum(map(bool, towels)), sum(towels)

    def FindArrangements(self, design, patterns):
        candidate = [1] + [0] * len(design)

        positions = [
            (i, pattern)
            for i, pattern in product(range(len(design)), patterns)
            if design[i:].startswith(pattern)
        ]

        for i, pattern in positions:
            candidate[i + len(pattern)] += candidate[i]

        return candidate[-1]

    def pt1(self, input):
        self.debug(input)

        res, _ = self.DesignTowels(input)

        return res

    def pt2(self, input):
        self.debug(input)

        _, res = self.DesignTowels(input)

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


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
