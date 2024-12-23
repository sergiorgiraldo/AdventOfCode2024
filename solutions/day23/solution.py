# puzzle prompt: https://adventofcode.com/2024/day/23

import sys
import time

sys.path.insert(0,"..")

import networkx as nx
from base.advent import *


class Solution(InputAsCSVSolution):
    _year = 2024
    _day = 23
    
    _is_debugging = False

    # this year I learned about networkx, what a great library
    def Go2LANParty(self, input):
        G = nx.Graph(input)
        self.debug(G.edges)
        self.debug(G.nodes)
        
        cliques = list(nx.enumerate_all_cliques(G))

        # Chief historian computer starts with "t"
        res1 = sum(any(a[0]=="t" for a in c) for c in cliques if len(c) == 3)
        res2 = ",".join(sorted(cliques[-1]))

        return res1, res2

    def pt1(self, input):
        self.debug(input)

        res1, _ = self.Go2LANParty(input)

        return res1

    def pt2(self, input):
        self.debug(input)

        _, res2 = self.Go2LANParty(input)

        return res2
        
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
    solution = Solution(separator="-")

    solution.part_1()
    
    solution.part_2()