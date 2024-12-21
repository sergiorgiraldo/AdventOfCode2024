import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = [
            "029A",
            "980A",
            "179A",
            "456A",
            "379A"
        ]
        self.assertEqual(solution.pt1(input), 126384, "Oops")

    # def test_part2(self):
        # input = ""
        # self.assertEqual(solution.pt2(input), "", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
