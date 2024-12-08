# puzzle prompt: https://adventofcode.com/2024/day/8

import sys
import time

sys.path.insert(0,"..")

from collections import defaultdict
from math import gcd

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 8
    
    _is_debugging = False

    def GetNodes(self, input):
        nodes = defaultdict(set)
        indexes = {}
        for i, row in enumerate(input):
            for j, c in enumerate(row):
                indexes[(i, j)] = 0
                if c != ".":
                    nodes[c].add((i, j))
        return nodes, indexes

    def FindUniqueLocations(self, input):
        def node_diff(a, b):
            return (a[0] - b[0], a[1] - b[1])        
        
        nodes, indexes = self.GetNodes(input)    

        antinodes = set()
        antinodes_antennas = set()

        for _, antennas in nodes.items():
            for antenna_1 in antennas:
                antinodes_antennas.add(antenna_1)
                for antenna_2 in antennas:
                    if antenna_1 == antenna_2:
                        continue

                    diff = node_diff(antenna_1, antenna_2)
                    div = gcd(abs(diff[0]), abs(diff[1])) # antinodes in line but not multiple of distance between antennas
                    diff = (diff[0] // div, diff[1] // div)
                    
                    try:
                        candidate = (antenna_1[0] + diff[0], antenna_1[1] + diff[1])
                        indexes[candidate]

                        antinodes.add(candidate)
                        antinodes_antennas.add(candidate)
                        
                        while True:
                            candidate = (candidate[0] + diff[0], candidate[1] + diff[1])
                            indexes[candidate]
                            antinodes_antennas.add(candidate)
                    except KeyError:
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

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()