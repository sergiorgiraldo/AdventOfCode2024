import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = [
            ["r, wr, b, g, bwu, rb, gb, br"],
            [
                "brwrr",
                "bggr",
                "gbbr",
                "rrbgbr",
                "ubwu",
                "bwurrg",
                "brgr",
                "bbrgwb"
            ]
        ]
        self.assertEqual(solution.pt1(input), 6, "Oops")

    def test_part2(self):
        input = [
            ["r, wr, b, g, bwu, rb, gb, br"],
            [
                "brwrr",
                "bggr",
                "gbbr",
                "rrbgbr",
                "ubwu",
                "bwurrg",
                "brgr",
                "bbrgwb"
            ]
        ]
        self.assertEqual(solution.pt2(input), 16, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
