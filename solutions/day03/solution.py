# puzzle prompt: https://adventofcode.com/2024/day/3

import re
import sys
import time

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsStringSolution):
    _year = 2024
    _day = 3

    _is_debugging = False

    def pt1(self, input):
        self.debug(input)

        regex = r"mul\((\d+),(\d+)\)"

        result = 0

        for a, b in re.findall(regex, input):
            result += int(a) * int(b)

        return result

    def pt2(self, input):
        self.debug(input)

        regex = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

        result = 0
        enabled = True

        for a, b, do, dont in re.findall(regex, input):
            if do or dont:
                enabled = bool(do)
            elif enabled:
                result += int(a) * int(b)

        return result

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
