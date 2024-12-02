# puzzle prompt: https://adventofcode.com/2024/day/2

import sys
import time

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsCSVSolution):
    _year = 2024
    _day = 2

    _is_debugging = False

    def CheckIfSafe(self, levels):
        is_safe = 0
        is_increasing = None
        for idx in range(0, len(levels) - 1):
            level_A = levels[idx]
            level_B = levels[idx + 1]

            if level_A > level_B:
                if is_increasing is None:
                    is_increasing = False
                elif is_increasing:
                    break
            else:
                if is_increasing is None:
                    is_increasing = True
                elif not is_increasing:
                    break

            diff = abs(level_A - level_B)
            if diff < 1 or diff > 3:
                break
        else:  # no break i.e. no increase nor decrease nor big differences
            is_safe = 1

        return is_safe

    def GetSafeLevels(self, input):
        total = 0

        for report in input:
            levels = [int(lvl) for lvl in report]

            total += self.CheckIfSafe(levels)

        return total

    def GetSafeLevelsWithTolerance(self, input):
        total = 0

        for report in input:
            levels = [int(lvl) for lvl in report]

            is_safe = self.CheckIfSafe(levels)

            if is_safe:
                total += 1
                continue
            # else try with tolerance

            # Brute force, always go for the simplest implementation
            for j in range(0, len(levels)):
                tolerance_levels = levels[:j] + levels[j + 1 :]

                is_safe = self.CheckIfSafe(tolerance_levels)

                if is_safe:
                    total += 1
                    break

        return total

    def pt1(self, input):
        self.debug(input)

        total = self.GetSafeLevels(input)

        return total

    def pt2(self, input):
        self.debug(input)

        total = self.GetSafeLevelsWithTolerance(input)

        return total

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
    solution = Solution(separator=" ")

    solution.part_1()

    solution.part_2()
