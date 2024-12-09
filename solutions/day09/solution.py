# puzzle prompt: https://adventofcode.com/2024/day/9

import sys
import time

sys.path.insert(0,"..")

from base.advent import *


class Solution(InputAsStringSolution):
    _year = 2024
    _day = 9
    
    _is_debugging = False

    def ComputeChecksum(self, space):
        total = 0
        for i, n in enumerate(space):
            if n == ".":
                continue
            total += int(n) * i
        return total

    def GetOriginalState(self, input):
        disk = []
        free = False
        id = 0
        free_space = {}
        for c in input:
            amount = int(c)
            if free:
                free_space[len(disk)] = amount
                for _ in range(amount):
                    disk.append(".")
            else:
                for _ in range(amount):
                    disk.append(str(id))
                id += 1
            free = not free # switch between free and used

        return disk, free_space
    
    def CompactByBlocks(self, input):
        disk, _ = self.GetOriginalState(input)

        for i, c in enumerate(disk): #find first free space
            if c == ".":
                l = i
                break

        r = len(disk) - 1
        while l < r:
            if disk[l] != ".":
                l += 1
                continue
            if disk[r] == ".":
                r -= 1
                continue
            disk[l] = disk[r]
            disk[r] = "."
            l += 1
            r -= 1

        return disk

    def CompactByFiles(self, input):
        disk, free_space = self.GetOriginalState(input)

        r = len(disk) - 1
        seen = set()
        while r > 0:
            if disk[r] == ".":
                r -= 1
                continue
            c = disk[r]
            if c in seen:
                r -= 1
                continue
            seen.add(c)

            file_size = 0
            while disk[r] == c and r >= 0:
                file_size += 1
                r -= 1

            candidates = [(k, v) for (k, v) in free_space.items() if k <= r and v >= file_size]
            if len(candidates) == 0:
                continue

            i, length = min(candidates, key=lambda x: x[0])
            for j in range(i, i + file_size):
                disk[j] = c
            for j in range(r + 1, r + 1 + file_size):
                disk[j] = "."
            del free_space[i]

            if file_size < length:
                free_space[i + file_size] = length - file_size

        return disk

    def pt1(self, input):
        self.debug(input)

        better_disk = self.CompactByBlocks(input)

        return self.ComputeChecksum(better_disk)

    def pt2(self, input):
        self.debug(input)

        better_disk = self.CompactByFiles(input)

        return self.ComputeChecksum(better_disk)
        
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