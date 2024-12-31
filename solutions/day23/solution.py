# puzzle prompt: https://adventofcode.com/2024/day/23

import sys
import time

sys.path.insert(0, "..")

from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx
from base.advent import *


class Solution(InputAsCSVSolution):
    _year = 2024
    _day = 23

    _is_debugging = False

    # Clique problem: https://en.wikipedia.org/wiki/Clique_problem
    # Bron–Kerbosch algorithm : https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    # so many solutions using this algorithm, lets learn it.
    # Algorithmm from networkx is Zhang, et al. (2005) (https://doi.org/10.1109/SC.2005.29)
    def part2_alternative(self, input):
        def parse_input():
            g = defaultdict(list)
            for line in input:
                u, v = line[0], line[1]
                g[u].append(v)
                g[v].append(u)
            return g

        def bron_kerbosch(r, p, x, cur):
            if not p and not x:
                return max(r, cur, key=len)

            pivot = next(iter(p | x))

            for v in list(p - set(G[pivot])):
                cur = max(
                    cur,
                    bron_kerbosch(r | {v}, p & set(G[v]), x & set(G[v]), cur),
                    key=len,
                )
                p -= {v}
                x |= {v}
            return cur

        G = parse_input()
        res = ",".join(sorted(bron_kerbosch(set(), set(G.keys()), set(), set())))

        print("\nAlternative solution for part 2")
        print("Part 2 ::", res)

    # this year I learned about networkx, what a great library
    def Go2LANParty(self, input):
        G = nx.Graph(input)

        self.debug(G.nodes)

        if self._is_debugging:
            # plotting the graph
            nx.draw(G, with_labels=True)
            plt.draw()
            plt.show()

        cliques = list(nx.enumerate_all_cliques(G))

        # Chief Historian computer starts with "t"
        # 3 connections is a magic number from the puzzle
        res1 = sum(any(a[0] == "t" for a in c) for c in cliques if len(c) == 3)
        res2 = ",".join(sorted(cliques[-1]))  # last one is the maximum clique

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


if __name__ == "__main__":
    solution = Solution(separator="-")

    solution.part_1()

    solution.part_2()

    solution.part2_alternative(solution.input)
