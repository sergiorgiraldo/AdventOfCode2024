# puzzle prompt: https://adventofcode.com/2024/day/15

import sys
import time

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsBlockSolution):
    _year = 2024
    _day = 15

    _is_debugging = False

    def GetCoord(self, position):
        return int(position.imag) * 100 + int(position.real)

    def GetGrid(self, input):
        grid = {}

        for y, row in enumerate(input):
            for x, cell in enumerate(row):
                location = x + y * 1j
                grid[location] = cell
                if cell == "@":
                    self.curr_location = location

        return grid

    def GetWiderGrid(self, input):
        wider_input = []

        for item in input:
            new_item = (
                item.replace("#", "##")
                .replace("O", "[]")
                .replace(".", "..")
                .replace("@", "@.")
            )
            wider_input.append(new_item)

        grid = self.GetGrid(wider_input)

        return grid

    def CollectBoxes(self, input, wider=False):
        offset = {">": 1, "<": -1, "^": -1j, "v": 1j}

        field, instructions = input

        if wider:
            grid = self.GetWiderGrid(field)
            condition = "["
        else:
            grid = self.GetGrid(field)
            condition = "O"

        for moves in instructions:
            for move in moves:
                if wider:
                    self.curr_location = self.WalkTheRobot_wh2(grid, offset[move])
                else:
                    self.curr_location = self.WalkTheRobot_wh1(grid, offset[move])

        gps = sum(
            [
                self.GetCoord(position)
                for position, cell in grid.items()
                if cell == condition
            ]
        )

        return gps

    def WalkTheRobot_wh1(self, grid, move):
        new_location = self.curr_location + move
        boxes_to_push = []
        while grid[new_location] == "O":
            new_location = new_location + move
            boxes_to_push.append(new_location)

        if grid[new_location] == "#":
            return self.curr_location
        if grid[new_location] == ".":
            for box in boxes_to_push:
                grid[box] = "O"
            grid[self.curr_location] = "."
            self.curr_location = self.curr_location + move
            grid[self.curr_location] = "@"
            return self.curr_location

    def WalkTheRobot_wh2(self, grid, move):
        if grid[self.curr_location + move] == "#":
            return self.curr_location

        locations_to_push_from = [self.curr_location]
        boxes_to_push = []

        while any(
            [grid[location + move] in "[]" for location in locations_to_push_from]
        ):
            if any(
                [grid[location + move] == "#" for location in locations_to_push_from]
            ):
                return self.curr_location
            new_locations_to_push_from = []
            for location in locations_to_push_from:
                boxes = []
                if grid[location + move] == "[":
                    boxes = [location + move]
                    if move in [1j, -1j]:
                        boxes.append(location + move + 1)
                elif grid[location + move] == "]":
                    boxes = [location + move]
                    if move in [1j, -1j]:
                        boxes.append(location + move - 1)
                boxes_to_push.extend(boxes)
                new_locations_to_push_from.extend(boxes)
            locations_to_push_from = new_locations_to_push_from

        if any([grid[box + move] == "#" for box in boxes_to_push]):
            return self.curr_location

        new_symbols = {}
        for box in boxes_to_push:
            symbol = grid[box]
            new_symbols[box + move] = symbol
        for box in boxes_to_push:
            grid[box] = "."
        for box, symbol in new_symbols.items():
            grid[box] = symbol

        grid[self.curr_location] = "."
        self.curr_location = self.curr_location + move
        grid[self.curr_location] = "@"

        return self.curr_location

    def pt1(self, input):
        self.debug(input)

        res = self.CollectBoxes(input)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.CollectBoxes(input, True)

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
