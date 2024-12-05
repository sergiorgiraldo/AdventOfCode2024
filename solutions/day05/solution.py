# puzzle prompt: https://adventofcode.com/2024/day/5

import sys
import time

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsBlockSolution):
    _year = 2024
    _day = 5

    _is_debugging = False

    def GetMiddlePages(self, input):
        rules = {tuple(r.split("|")) for r in input[0]}

        totals = [0, 0]

        for pages in input[1]:
            current, fixed = pages.split(","), []

            for page in (
                current * 20
            ):  # hack: the amount of pages is little but there are a lot of rules
                # i would need to iterate over and over again to find the correct pages
                # if I replicate the pages, then I can iterate over the rules using all
                if page in fixed:
                    continue  # since I replicated the pages, i need to account for duplicates

                if all(b in fixed for b, a in rules if page == a and b in current):
                    fixed.append(page)

            totals[fixed != current] += int(
                fixed[len(fixed) // 2]
            )  # in part 1, we want the sum of correct pages (new == old)
            # in part 2, we want the sum of incorrect pages (new != old)
            # so, flip the bool

        return totals

    def pt1(self, input):
        self.debug(input)

        totals = self.GetMiddlePages(input)

        return totals[0]

    def pt2(self, input):
        self.debug(input)

        totals = self.GetMiddlePages(input)

        return totals[1]

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
