import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = [
                    ["Register A: 729", "Register B: 0","Register C: 0"],
                    ["Program: 0,1,5,4,3,0"]
                ]
        self.assertEqual(solution.pt1(input), "4,6,3,5,6,3,5,2,1,0", "Oops")

    def test_part2(self):
        input = [
                    ["Register A: 2024", "Register B: 0","Register C: 0"],
                    ["Program: 0,3,5,4,3,0"]
                ]
        self.assertEqual(solution.pt2(input), 117440, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
