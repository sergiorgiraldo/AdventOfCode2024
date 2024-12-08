# puzzle prompt: https://adventofcode.com/2024/day/4

import sys
import time

sys.path.insert(0, "..")

from collections import defaultdict

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 4

    _is_debugging = False

    def GetMatrix(self, input):
        m = defaultdict(lambda: ".")

        for i, line in enumerate(input):
            for j, c in enumerate(line):
                m[i + 1j * j] = c  # treat each cell as a complex number
        
        k = list(m.keys())
        
        return m, k

    # XMAS SAMX
    # X S   X        S
    # M A    M      A
    # A M     A    M
    # S X      S  X
    # horizontal, vertical or diagonal
    def FindXMAS(self, input):
        matrix, coords = self.GetMatrix(input)

        self.debug(matrix)
        count = 0

        for offset in (1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 - 1j, -1 + 1j):
            for coord in coords:
                count += (
                    matrix[coord]                   == "X"
                    and matrix[coord + offset]      == "M"
                    and matrix[coord + 2 * offset]  == "A"
                    and matrix[coord + 3 * offset]  == "S"
                )

        return count

    # M S
    #  A
    # M S
    # find mas in cross
    def FindMSAMS(self, input):
        matrix, coords = self.GetMatrix(input)

        count = 0
        for coord in coords:
            count += (
                matrix[coord] == "A"
                and (
                    (matrix[coord - 1 - 1j] == "M" and matrix[coord + 1 + 1j]    == "S")
                    or (matrix[coord - 1 - 1j] == "S" and matrix[coord + 1 + 1j] == "M")
                )
                and (
                    (matrix[coord - 1 + 1j] == "M" and matrix[coord + 1 - 1j]    == "S")
                    or (matrix[coord - 1 + 1j] == "S" and matrix[coord + 1 - 1j] == "M")
                )
            )

        return count

    def pt1(self, input):
        self.debug(input)

        count = self.FindXMAS(input)

        return count

    def pt2(self, input):
        self.debug(input)

        count = self.FindMSAMS(input)

        return count

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
