import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = [
            ["kh", "tc"],
            ["qp", "kh"],
            ["de", "cg"],
            ["ka", "co"],
            ["yn", "aq"],
            ["qp", "ub"],
            ["cg", "tb"],
            ["vc", "aq"],
            ["tb", "ka"],
            ["wh", "tc"],
            ["yn", "cg"],
            ["kh", "ub"],
            ["ta", "co"],
            ["de", "co"],
            ["tc", "td"],
            ["tb", "wq"],
            ["wh", "td"],
            ["ta", "ka"],
            ["td", "qp"],
            ["aq", "cg"],
            ["wq", "ub"],
            ["ub", "vc"],
            ["de", "ta"],
            ["wq", "aq"],
            ["wq", "vc"],
            ["wh", "yn"],
            ["ka", "de"],
            ["kh", "ta"],
            ["co", "tc"],
            ["wh", "qp"],
            ["tb", "vc"],
            ["td", "yn"],
        ]
        self.assertEqual(solution.pt1(input), 7, "Oops")

    def test_part2(self):
        input = [
            ["kh", "tc"],
            ["qp", "kh"],
            ["de", "cg"],
            ["ka", "co"],
            ["yn", "aq"],
            ["qp", "ub"],
            ["cg", "tb"],
            ["vc", "aq"],
            ["tb", "ka"],
            ["wh", "tc"],
            ["yn", "cg"],
            ["kh", "ub"],
            ["ta", "co"],
            ["de", "co"],
            ["tc", "td"],
            ["tb", "wq"],
            ["wh", "td"],
            ["ta", "ka"],
            ["td", "qp"],
            ["aq", "cg"],
            ["wq", "ub"],
            ["ub", "vc"],
            ["de", "ta"],
            ["wq", "aq"],
            ["wq", "vc"],
            ["wh", "yn"],
            ["ka", "de"],
            ["kh", "ta"],
            ["co", "tc"],
            ["wh", "qp"],
            ["tb", "vc"],
            ["td", "yn"],
        ]
        self.assertEqual(solution.pt2(input), "co,de,ka,ta", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
