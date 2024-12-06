# puzzle prompt: https://adventofcode.com/2024/day/6

import sys
import time

sys.path.insert(0,"..")

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2024
    _day = 6
    
    _is_debugging = False

    def GetMaze(self, input):
        maze = {}

        for row, line in enumerate(input):
            for col, cell in enumerate(line):
                maze[(row, col)] = cell
                if cell == "^":
                    curr = (row, col)

        return maze, curr

    # just walk the maze until out of bounds
    def GetGuardRoute(self,input):
        def Set():
            maze[curr] = "."
            maze[curr] = "^"
            visited.add(curr)

        maze, curr = self.GetMaze(input)
        visited = set()

        height = len(input)
        width = len(input[0])

        direction = "up"
        visited.add(curr)

        while True:
            if direction == "up":
                if curr[0] - 1 < 0: # out of bounds
                    break
                elif maze[(curr[0] - 1, curr[1])] == "#":
                    direction = "right"
                else:
                    curr = (curr[0] - 1, curr[1])
                    Set()
            elif direction == "down":
                if curr[0] + 1 >= height:# out of bounds
                    break
                elif maze[(curr[0] + 1, curr[1])] == "#":
                    direction = "left"
                else:
                    curr = (curr[0] + 1, curr[1])
                    Set()
            elif direction == "right":
                if curr[1] + 1 >= width:# out of bounds
                    break
                elif maze[(curr[0], curr[1] + 1)] == "#":
                    direction = "down"
                else:
                    curr = (curr[0], curr[1] + 1)
                    Set()
            elif direction == "left":
                if curr[1] - 1 < 0:# out of bounds
                    break
                elif maze[(curr[0], curr[1] - 1)] == "#":
                    direction = "up"
                else:
                    curr = (curr[0], curr[1] - 1)
                    Set()

        return len(visited)

    # took the simplest implementation, i make the guard walk and check if
    # he already visited the cell
    def TrapTheGuard(self, input):
        def InLoop():
            if (curr, direction) in visited:
                return True
            else:
                visited.add((curr, direction))
                return False
            
        maze, start = self.GetMaze(input)
        obstructions = 0

        height = len(input)
        width = len(input[0])

        for cell in maze.keys():
            if maze[cell] != ".":
                continue

            maze[cell] = "#" #obstruction

            curr = start
            direction = "up"
            visited = set()
            visited.add((curr, direction))

            while True:
                if direction == "up":
                    if curr[0] - 1 < 0:
                        break
                    elif maze[(curr[0] - 1, curr[1])] == "#":
                        direction = "right"
                    else:
                        maze[curr] = "."
                        curr = (curr[0] - 1, curr[1])
                        maze[curr] = "^"

                        if InLoop():obstructions += 1;break
                elif direction == "down":
                    if curr[0] + 1 >= height:
                        break
                    elif maze[(curr[0] + 1, curr[1])] == "#":
                        direction = "left"
                    else:
                        maze[curr] = "."
                        curr = (curr[0] + 1, curr[1])
                        maze[curr] = "^"

                        if InLoop():obstructions += 1;break
                elif direction == "right":
                    if curr[1] + 1 >= width:
                        break
                    elif maze[(curr[0], curr[1] + 1)] == "#":
                        direction = "down"
                    else:
                        maze[curr] = "."
                        curr = (curr[0], curr[1] + 1)
                        maze[curr] = "^"

                        if InLoop():obstructions += 1;break
                elif direction == "left":
                    if curr[1] - 1 < 0:
                        break
                    elif maze[(curr[0], curr[1] - 1)] == "#":
                        direction = "up"
                    else:
                        maze[curr] = "."
                        curr = (curr[0], curr[1] - 1)
                        maze[curr] = "^"

                        if InLoop():obstructions += 1;break

            # restore the original cells
            maze[curr] = "."
            maze[cell] = "." 

        return obstructions

    def pt1(self, input):
        self.debug(input)

        res = self.GetGuardRoute(input)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.TrapTheGuard(input)

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