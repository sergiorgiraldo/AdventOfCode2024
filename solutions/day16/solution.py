# puzzle prompt: https://adventofcode.com/2024/day/16

import sys
import time

sys.path.insert(0,"..")

from collections import defaultdict, deque
from enum import Enum
from heapq import heappop, heappush
from itertools import product

from base.advent import *


class Face(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def RotateCounterClockwise(self):
        return Face((self.value - 1) % 4)

    def RotateClockwise(self):
        return Face((self.value + 1) % 4)

class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 16
    
    _is_debugging = False

    DIRECTION = {
        Face.NORTH: (-1,  0),
        Face.EAST:  ( 0,  1),
        Face.SOUTH: ( 1,  0),
        Face.WEST:  ( 0, -1)
    }

    def FindRobot(self, grid, face):
        for row, col in product(range(len(grid)), range(len(grid[0]))):
            if grid[row][col] == face:
                return row, col

        raise ValueError("No robot found")

    def WalkTheMaze(self, input):
        start_row, start_col = self.FindRobot(input, "S")
        end_row, end_col = self.FindRobot(input, "E")

        pq = [(0, start_row, start_col, Face.EAST.value)]
        best_scores = {}

        while pq:
            score, r, c, facing = heappop(pq)
            facing = Face(facing)

            if score >= best_scores.get((r, c, facing), float("inf")):
                continue

            best_scores[(r, c, facing)] = score

            if (r, c) == (end_row, end_col):
                return score

            offset_r, offset_c = self.DIRECTION[facing]
            new_r, new_c = r + offset_r, c + offset_c

            if (
                0 <= new_r < len(input)
                and 0 <= new_c < len(input[0])
                and input[new_r][new_c] != "#"
            ):
                heappush(pq, (score + 1, new_r, new_c, facing.value))

            new_facing = facing.RotateClockwise()
            heappush(pq, (score + 1000, r, c, new_facing.value))

            new_facing = facing.RotateCounterClockwise()
            heappush(pq, (score + 1000, r, c, new_facing.value))

        return -1

    def FindSeat(self, grid):
        start_row, start_col = self.FindRobot(grid, "S")
        end_row, end_col = self.FindRobot(grid, "E")

        pq = [(0, start_row, start_col, Face.EAST.value, [])]
        best_scores = {}
        min_end_score = float("inf")
        seats = {}

        while pq:
            score, r, c, facing, path = heappop(pq)
            facing = Face(facing)

            if (r, c) == (end_row, end_col):
                if score <= min_end_score:
                    min_end_score = score
                    if min_end_score not in seats:
                        seats[min_end_score] = set()
                    seats[min_end_score].update(path)
                continue

            if best_scores.get((r, c, facing), float("inf")) < score:
                continue

            best_scores[(r, c, facing)] = score

            offset_r, offset_c = self.DIRECTION[facing]
            new_r, new_c = r + offset_r, c + offset_c

            if (
                0 <= new_r < len(grid)
                and 0 <= new_c < len(grid[0])
                and grid[new_r][new_c] != "#"
            ):
                heappush(pq, (score + 1, new_r, new_c, facing.value, path + [(r, c)]))

            new_facing = facing.RotateClockwise()
            heappush(pq, (score + 1000, r, c, new_facing.value, path + [(r, c)]))

            new_facing = facing.RotateCounterClockwise()
            heappush(pq, (score + 1000, r, c, new_facing.value, path + [(r, c)]))

        return len(seats[min_end_score]) + 1

    def pt1(self, input):
        self.debug(input)

        res = self.WalkTheMaze(input)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.FindSeat(input)

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