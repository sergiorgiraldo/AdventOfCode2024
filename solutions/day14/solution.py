# puzzle prompt: https://adventofcode.com/2024/day/14

import sys
import time

sys.path.insert(0,"..")

import operator
import re
from collections import Counter
from functools import reduce

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 14
    
    _is_debugging = False

    WIDTH = 101 #magic numbers from the puzzle
    HEIGHT = 103
  
    def GetSpaceForTest(self):
        self.WIDTH = 11 #magic numbers from the puzzle
        self.HEIGHT = 7

    def GetRobots(self, input):
        robots = []

        for line in input:
            px, py, vx, vy = map(int, re.findall(r"(-?\d+)", line))
            robots.append((px, py, vx, vy))

        return robots

    def EvaluatePosition(self, robot, time):
        px, py, vx, vy = robot

        return ((px + vx * time) % self.WIDTH, (py + vy * time) % self.HEIGHT)

    def FindQuadrant(self, position):
        px, py = position
        
        if px == self.WIDTH // 2 or py == self.HEIGHT // 2:
            return None
        
        return (px < self.WIDTH // 2, py < self.HEIGHT // 2)
    
    def CountRobots(self, input):
        robots = self.GetRobots(input)

        quadrants = Counter()

        for robot in robots:
            new_position = self.EvaluatePosition(robot, 100)
            quadrant = self.FindQuadrant(new_position)
            if quadrant is not None:
                quadrants[quadrant] += 1

        safety_factor = reduce(operator.mul, map(lambda v: v, quadrants.values()), 1)

        return safety_factor

    def FindAdjacent(self, positions):
        adjacents = 0
        pos_set = set(positions)

        for y in range(self.HEIGHT):
            for x in range(self.WIDTH - 1):
                if (x, y) in pos_set and (x + 1, y) in pos_set:
                    adjacents += 1
        
        return adjacents

    #the tree must be a set of connected positions i.e. adjacent to each other
    def FindEasterEgg(self, input):
        robots = self.GetRobots(input)

        for time in range(10000): #arbitrary time limit, tried with 1000, 5000, then 10000
            positions = [self.EvaluatePosition(robot, time) for robot in robots]
            adjacencies = self.FindAdjacent(positions)
            if adjacencies > 100: #arbitrary number of points
                return time
        
        raise Exception("Easter egg not found")

    def pt1(self, input):
        self.debug(input)

        safety_factor = self.CountRobots(input)

        return safety_factor

    def pt2(self, input):
        self.debug(input)

        time = self.FindEasterEgg(input)

        return time
        
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