# puzzle prompt: https://adventofcode.com/2024/day/12

import sys
import time

sys.path.insert(0,"..")

from collections import defaultdict

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 12
    
    _is_debugging = False

    # complex numbers, same idea from day 04
    def GetMatrix(self,input):
        matrix = defaultdict()

        for i, line in enumerate(input):
            for j, c in enumerate(line):
                matrix[i + 1j * j] = c  

        return matrix

    def FindAdjacent(self, coord, offsets=[1, 1j, -1, -1j]):
        return [coord + offset for offset in offsets]

    def FillRegion(self, matrix, c):
        self.visited.add(c)
        region = [c]

        for adjacent in self.FindAdjacent(c):
            if matrix.get(adjacent) == matrix[c] and adjacent not in self.visited:
                region += self.FillRegion(matrix, adjacent)
        
        return region

    def CheckGarden(self, input):
        s1 = s2 = 0

        # x . x
        # . o .
        # x . x
        plot_corners = [.5+.5j, .5-.5j, -.5+.5j, -.5-.5j]

        self.visited = set()

        matrix = self.GetMatrix(input)

        for coord, _ in matrix.items():
            self.debug(coord)

            if coord in self.visited: continue

            perimeter, corners = 0, set()

            for r in (region := self.FillRegion(matrix, coord)):
                perimeter += sum(adjacent not in region for adjacent in self.FindAdjacent(r))

                for corner in self.FindAdjacent(r, plot_corners):
                    k = [adjacent for adjacent in self.FindAdjacent(corner, plot_corners) if adjacent in region]
                    self.debug("adjacents", k)

                    #  ⎯
                    # | |

                    #  _
                    # |_

                    # _ 
                    # _|

                    #  | |
                    #   ⎯
                    if len(k) in [1, 3]:
                        corners.add(corner)
                    # Each straight section of fence counts as a side, regardless of how long it is.
                    elif abs(k[0] - k[1]) > 1:
                        self.debug("else",corner + 0.1)
                        self.debug("else",corner + 0.1)
                        corners.add(corner)
                        corners.add(corner + 0.1)

            s1 += perimeter * len(region)
            s2 += len(corners) * len(region)
        
        return s1, s2

    def pt1(self, input):
        self.debug(input)

        res, _ = self.CheckGarden(input)

        return res

    def pt2(self, input):
        self.debug(input)

        _, res = self.CheckGarden(input)

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

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()