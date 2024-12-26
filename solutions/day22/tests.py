import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = [1, 10, 100, 2024]
        self.assertEqual(solution.pt1(input), 37327623, "Oops")

    def test_part2(self):
        input = [1, 2, 3, 2024]
        self.assertEqual(solution.pt2(input), 23, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
