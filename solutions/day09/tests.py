import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = "2333133121414131402"
        self.assertEqual(solution.pt1(input), 1928, "Oops")

    def test_part2(self):
        input = "2333133121414131402"
        self.assertEqual(solution.pt2(input), 2858, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
