# puzzle prompt: https://adventofcode.com/2024/day/25

import sys
import time

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsBlockSolution):
    _year = 2024
    _day = 25

    _is_debugging = False

    def FindPairs(self, input):
        locks = set()
        keys = set()

        max_height = len(input[0][0])

        for schematic in input:
            heights = tuple(
                len([pin[i] for pin in schematic if pin[i] == "#"]) - 1
                for i in range(len(schematic[0]))
            )

            is_lock = "." not in schematic[0]

            locks.add(heights) if is_lock else keys.add(heights)

        fit_count = sum(
            map(
                lambda lock: sum(self.SeeIfFits(lock, key, max_height) for key in keys),
                locks,
            )
        )

        return fit_count

    def SeeIfFits(self, lock, key, max_height):
        return all(map(lambda i: lock[i] + key[i] <= max_height, range(len(lock))))

    def pt1(self, input):
        self.debug(input)

        res = self.FindPairs(input)

        return res

    def pt2(self, input):
        self.debug(input)

        return ""

    def part_1(self):
        start_time = time.time()

        res = self.pt1(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.pt2(self.input)

        end_time = time.time()

        # self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    # solution.part_2()
