import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
        self.assertEqual(solution.pt1(input), 121, "Oops")

    def test_part2(self):
        input = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
        self.assertEqual(solution.pt2(input), 31, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
