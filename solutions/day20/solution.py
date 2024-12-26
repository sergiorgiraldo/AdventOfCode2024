# puzzle prompt: https://adventofcode.com/2024/day/20

import sys
import time

sys.path.insert(0, "..")

from collections import defaultdict

from base.advent import *
from networkx import Graph, shortest_path_length


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 20

    _is_debugging = False

    def GetMatrix(self, input):
        m = defaultdict()

        for i, line in enumerate(input):
            for j, c in enumerate(line):
                coord = i + 1j * j
                m[coord] = c

                if c == "S":
                    start = coord

        return m, start

    def FindCheats(self, input, threshold=100):
        matrix, start = self.GetMatrix(input)
        offsets = [1, 1j, -1, -1j]

        graph = Graph()

        for coord in matrix:
            for offset in offsets:
                if matrix[coord] != "#" != matrix[coord + offset]:
                    graph.add_edge(coord, coord + offset)

        path = shortest_path_length(graph, start).items()

        s1 = s2 = 0

        # check how much can be saved
        for c1, dist1 in path:
            for c2, dist2 in path:
                diff = int(abs((c2 - c1).real) + abs((c2 - c1).imag))
                if dist2 - dist1 - diff >= threshold:
                    s1 += diff <= 2  # magic number from the puzzle
                    s2 += diff <= 20  # magic number from the puzzle

        return s1, s2

    def pt1(self, input):
        self.debug(input)

        res, _ = self.FindCheats(input)

        return res

    def pt2(self, input):
        self.debug(input)

        _, res = self.FindCheats(input)

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
