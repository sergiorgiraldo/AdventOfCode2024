# puzzle prompt: https://adventofcode.com/2024/day/21

import sys
import time

sys.path.insert(0,"..")

from collections import Counter

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 21
    
    _is_debugging = False

#numeric pad
#+---+---+---+
#| 7 | 8 | 9 |
#+---+---+---+
#| 4 | 5 | 6 |
#+---+---+---+
#| 1 | 2 | 3 |
#+---+---+---+
#    | 0 | A |
#    +---+---+

#direction pad
#    +---+---+
#    | ^ | A |
#+---+---+---+
#| < | v | > |
#+---+---+---+

    # set coordinates for the number pad and the direction pad
    def Setup(self):
        num_pad_lines = ["789", "456", "123", " 0A"] # from the puzzle
        num_pad = {(i,j):c for i,line in enumerate(num_pad_lines) for j,c in enumerate(line) if c != " "}
        num_pad.update({v:k for k,v in num_pad.items()})

        dir_pad_lines = [" ^A", "<v>"] # from the puzzle
        dir_pad = {(i,j):c for i,line in enumerate(dir_pad_lines) for j,c in enumerate(line) if c != " "}
        dir_pad.update({v:k for k,v in dir_pad.items()})
        
        return num_pad, dir_pad

    def MoveArm(self, source, target, pad):
        target_Y, target_X = pad[target]
        source_Y, source_X = pad[source]

        distance_Y = target_Y - source_Y
        distance_X = target_X - source_X
        
        vert  = "v" * distance_Y + "^" * -distance_Y
        horiz = ">" * distance_X + "<" * -distance_X
        
        if distance_X > 0 and (target_Y,source_X) in pad:
            return vert+horiz+"A"
        
        if (source_Y,target_X) in pad:
            return horiz+vert+"A"
        
        if (target_Y,source_X) in pad:
            return vert+horiz+"A"
        
    def FindRoute(self, path, pad, which):
        route = []
        start = "A"
        
        for end in path:
            route.append(self.MoveArm(start,end,pad))
            start = end
        
        return "".join(route) if which == 1 else Counter(route)

    def GetRoutesForCodes(self,input):
        num_pad, _ = self.Setup()

        routes = [self.FindRoute(line, num_pad, 1) for line in input]

        return routes

    def TypeCodesForOneRobot(self, input):
        _, dir_pad = self.Setup()

        routes = self.GetRoutesForCodes(input)
        
        robot_1_routes = [self.FindRoute(route, dir_pad, 1) for route in routes]
        robot_2_routes = [self.FindRoute(route, dir_pad, 1) for route in robot_1_routes]

        res = sum(len(route)*int(line[:-1]) for route, line in zip(robot_2_routes,input))
        
        return res

    def TypeCodesForManyRobots(self, lines):
        def len_(route):
            return sum(len(k)*v for k,v in route.items())

        _, dir_pad = self.Setup()
        
        routes = self.GetRoutesForCodes(lines)

        robot_routes = [Counter([route]) for route in routes]
        
        for _ in range(25): # magic number from the puzzle
            new_routes = []
            for route_counter in robot_routes:
                new_route = Counter()
                for sub_route, qty in route_counter.items():
                    new_counts = self.FindRoute(sub_route, dir_pad, 2)
                    for k in new_counts:
                        new_counts[k] *= qty
                    new_route.update(new_counts)
                new_routes.append(new_route)
            robot_routes = new_routes

        res = sum(len_(route)*int(line[:-1]) for route, line in zip(robot_routes,lines))

        return res

    def pt1(self, input):
        self.debug(input)

        res = self.TypeCodesForOneRobot(input)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.TypeCodesForManyRobots(input)

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