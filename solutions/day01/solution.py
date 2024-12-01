# puzzle prompt: https://adventofcode.com/2024/day/1

import sys
import time

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 1

    _is_debugging = True

    def getArrays(self, input):
        column1 = []
        column2 = []

        for line in input:
            ids = line.split("   ")
            column1 += [int(ids[0])]
            column2 += [int(ids[1])]

        column1.sort()
        column2.sort()

        return column1, column2

    def getDistance(self, input):
        column1, column2 = self.getArrays(input)

        distance = 0

        for i in range(len(column1)):
            distance += abs(column1[i] - column2[i])

        return distance

    def getSimilarity(self, input):
        column1, column2 = self.getArrays(input)

        similarity = 0

        for i in range(len(column1)):
            similarity += column1[i] * sum(id == column1[i] for id in column2)

        return similarity

    def pt1(self, input):
        self.debug(input)

        return self.getDistance(input)

    def pt2(self, input):
        self.debug(input)

        return self.getSimilarity(input)

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
