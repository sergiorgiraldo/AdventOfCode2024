# puzzle prompt: https://adventofcode.com/2024/day/24

'''
Part 1
The output wires depend on two input wires, forming a tree structure where input wires 
(x's and y's) are the leaves. 
By processing each gate or output in order of tree depth, dependencies are resolved as we progress. This structure, though perhaps overly meticulous for simulation, ensures reliability.

Part 2
The puzzle is a ripple carry adder (a circuit to add 2 binary numbers), specifically a 44-block variant. 
Output wires correspond to internal configurations identifiable by operands (^, &, |) and 
inputs. 
The function iterates from lower to higher-indexed blocks, ensuring computation flows from 
LSB to MSB. Higher-indexed blocks depend on the correctness of lower-indexed ones, i.e., if higher blocks
are correct, lower blocks must be correct.

Verification occurs when specific gates output the z wires. 
If correct, all dependent wires are correct, adding relevant wires to a correct set. 
If not, the last correct block and correct set are returned.

So:
- Execute the function once to establish base correctness.
- Swap output wires of gate pairs not in the correct set.
- Re-run the function to check improvements and validate swaps.
- Repeat this process four times (there are 4 gates to swap) to achieve a fully functional ripple-carry adder.
'''

import sys
import time

sys.path.insert(0,"..")

import re
from itertools import combinations

from base.advent import *


class Solution(InputAsBlockSolution):
    _year = 2024
    _day = 24
    
    _is_debugging = False

    def Parse(self, input):
        inputs, gates = input[0], input[1]

        input_pattern = r"([xy]\d\d): ([10])"
        finished = {}
        for line in inputs:
            match = re.search(input_pattern, line)
            input_name, val = match.groups()
            val = int(val)
            finished[input_name] = val

        gate_pattern = r"([a-z0-9]{3}) ([XORAND]+) ([a-z0-9]{3}) -> ([a-z0-9]{3})"
        ops = set()
        op_list = []
        for line in gates:
            match = re.search(gate_pattern, line)
            x1, op, x2, res = match.groups()
            ops.add((x1, x2, res, op))
            op_list.append((x1, x2, res, op))

        return finished, ops, op_list

    def GetDepth(self, reg, finished, parents):
        if reg in finished:
            return 0

        x1, x2 = parents[reg]

        # Need to finish x1 and x2 first
        return max(self.GetDepth(x1, finished, parents), self.GetDepth(x2, finished, parents)) + 1

    # Dependencies create a hierarchical arrangement, 
    # with initial nodes at the base. Handle nodes based on their hierarchy level.
    # This ensures operand availability when arriving at any particular gate.
    def Simulate(self, input):
        finished, ops, _ = self.Parse(input)

        # Calculating the structure of the tree
        parents = {}
        op_map = {}  # Mapping output name to corresponding operation (XOR, OR, AND)
        for x1, x2, res, op in ops:
            parents[res] = (x1, x2)
            op_map[res] = op

        # Calculate in optimal order
        vars = [(res, self.GetDepth(res, finished, parents)) for _, _, res, _ in ops]
        vars.sort(key=lambda x: x[1])  # Process lower depth first

        for reg, _ in vars:
            x1, x2 = parents[reg]
            v1, v2 = finished[x1], finished[x2]

            op = op_map[reg]

            val = {
                "XOR": lambda a, b: a ^ b,
                "OR": lambda a, b: a | b,
                "AND": lambda a, b: a & b,
            }[op](v1, v2)

            finished[reg] = val

        # Concatenate outputs -> binary -> decimal
        regs = list(finished.items())
        regs.sort(key=lambda x: x[0])
        num_out = int(str(regs[-1][0])[-2:]) + 1
        bin_str = "".join(str(val) for _, val in regs[-num_out:])
        return int(bin_str[::-1], 2)
        
    # Examine the operation sequence to gauge progress and record wires requiring accuracy.
    # Identified corresponding input lines for the ripple-carry adder wires.
    # The "Validation point" is when the output aligns with z15 or another reference --
    # ensuring all dependent outputs are accurate.
    def SeeHowFarWeMade(self, op_list):
        ops = {}
        for x1, x2, res, op in op_list:
            ops[(frozenset([x1, x2]), op)] = res  # hashability reason

        # here, x1 and x2 can be provided in any order :)
        def get_res(x1, x2, op):
            return ops.get((frozenset([x1, x2]), op), None)

        carries = {}
        correct = set()
        prev_intermediates = set()
        for i in range(45):
            pos = f"0{i}" if i < 10 else str(i)
            predigit = get_res(f"x{pos}", f"y{pos}", "XOR")
            precarry1 = get_res(f"x{pos}", f"y{pos}", "AND")
            if i == 0:
                # only two, XOR and AND
                carries[i] = precarry1
                continue
            digit = get_res(carries[i - 1], predigit, "XOR")
            if digit != f"z{pos}":
                return i - 1, correct

            # If it DID work, we know carries[i-1] and predigit were correct
            correct.add(carries[i - 1])
            correct.add(predigit)
            # Also add variables from previous position's ripple-carry adder module
            for wire in prev_intermediates:
                correct.add(wire)

            # Next, we compute the carries
            precarry2 = get_res(carries[i - 1], predigit, "AND")
            carry_out = get_res(precarry1, precarry2, "OR")
            carries[i] = carry_out
            prev_intermediates = set([precarry1, precarry2])

        return 45, correct

    def Swap(self, input):
        _, _, op_list = self.Parse(input)

        swaps = set()

        base, base_used = self.SeeHowFarWeMade(op_list)  # Everything up to 20 is fine
        for _ in range(4): # 4 pairs of gates to swap
            # try swapping
            for i, j in combinations(range(len(op_list)), 2):
                x1_i, x2_i, res_i, op_i = op_list[i]
                x1_j, x2_j, res_j, op_j = op_list[j]
                # Don't switch z00 out
                if "z00" in (res_i, res_j):
                    continue
                # Don't switch if these wires have already been used
                if res_i in base_used or res_j in base_used:
                    continue
                # Switch output wires
                op_list[i] = x1_i, x2_i, res_j, op_i
                op_list[j] = x1_j, x2_j, res_i, op_j
                attempt, attempt_used = self.SeeHowFarWeMade(op_list)
                if attempt > base:
                    # print(f"Swap. Got to a higher block: {attempt}")
                    swaps.add((res_i, res_j))
                    base, base_used = attempt, attempt_used
                    break
                # Switch output wires back
                op_list[i] = x1_i, x2_i, res_i, op_i
                op_list[j] = x1_j, x2_j, res_j, op_j

        return ",".join(sorted(sum(swaps, start=tuple())))

    def pt1(self, input):
        self.debug(input)

        res = self.Simulate(input)

        return res

    def pt2(self, input):
        self.debug(input)

        res = self.Swap(input)

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