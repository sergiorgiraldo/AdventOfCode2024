# puzzle prompt: https://adventofcode.com/2024/day/8

import sys
import time

sys.path.insert(0, "..")

from collections import defaultdict
from math import gcd

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 8

    _is_debugging = False

    def GetNodes(self, input):
        nodes = defaultdict(set)
        map = {}
        for i, row in enumerate(input):
            for j, c in enumerate(row):
                map[(i, j)] = 0
                if c != ".":
                    nodes[c].add((i, j))
        return nodes, map

    def FindUniqueLocations(self, input):
        def get_distance(a, b):
            return (a[0] - b[0], a[1] - b[1])

        nodes, map = self.GetNodes(input)

        antinodes = set()
        antinodes_antennas = set()

        for _, antennas in nodes.items():
            for antenna_1 in antennas:
                antinodes_antennas.add(antenna_1)
                for antenna_2 in antennas:
                    if antenna_1 == antenna_2:
                        continue
                    distance = get_distance(antenna_1, antenna_2)
                    div = gcd(
                        abs(distance[0]), abs(distance[1])
                    )  # antinodes in line but not multiple of distance between antennas
                    distance = (distance[0] // div, distance[1] // div)

                    try:
                        candidate = (
                            antenna_1[0] + distance[0],
                            antenna_1[1] + distance[1],
                        )
                        map[candidate]  # hack: check out of bounds

                        antinodes.add(candidate)
                        antinodes_antennas.add(candidate)

                        while True:
                            # antinodes in line: i keep adding the distance until out of bounds
                            candidate = (
                                candidate[0] + distance[0],
                                candidate[1] + distance[1],
                            )
                            map[candidate]  # hack: check out of bounds

                            antinodes_antennas.add(candidate)
                    except (
                        KeyError
                    ):  # thrown when out of bounds (when accesing the map)
                        continue

        return antinodes, antinodes_antennas

    def pt1(self, input):
        self.debug(input)

        res, _ = self.FindUniqueLocations(input)

        return len(res)

    def pt2(self, input):
        self.debug(input)

        _, res = self.FindUniqueLocations(input)

        return len(res)

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
