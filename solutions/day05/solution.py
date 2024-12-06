# puzzle prompt: https://adventofcode.com/2024/day/5

import sys
import time

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsBlockSolution):
    _year = 2024
    _day = 5

    _is_debugging = False

    def GetMiddlePages(self, input, reorder = False):
        rules = {tuple(r.split("|")) for r in input[0]}

        totals = [0, 0]

        longest = len(max(input[1], key=lambda x: len(x.split(","))).split(",")) if reorder else 1

        for pages in input[1]:
            original, fixed = pages.split(","), []

            # hack: there are a lot of rules
            # I would need to iterate over and over again to order pages for part 2,
            # if I replicate the pages, then I can iterate over the rules using all.
            # I use the longest line for the worst case when pages are all wrong in reverse order
            for page in (original * longest):  
                if reorder and page in fixed:
                    continue  # since I replicated the pages for part 2, i need to account for duplicates

                if all(b in fixed for b, a in rules if page == a and b in original):
                    fixed.append(page)

            # in part 1, we want the sum of middle pages without reorder (fixed == current)
            # in part 2, we want the sum of middle pages with reorder (fixed != current)
            # so, flip the bool
            totals[fixed != original] += int(fixed[len(fixed) // 2])  

        return totals

    def pt1(self, input):
        self.debug(input)

        totals = self.GetMiddlePages(input)

        return totals[0]

    def pt2(self, input):
        self.debug(input)

        totals = self.GetMiddlePages(input, True)

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
