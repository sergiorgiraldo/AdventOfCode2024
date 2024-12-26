import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        input = [
            ["Button A: X+94, Y+34", "Button B: X+22, Y+67", "Prize: X=8400, Y=5400"],
            ["Button A: X+26, Y+66", "Button B: X+67, Y+21", "Prize: X=12748, Y=12176"],
            ["Button A: X+17, Y+86", "Button B: X+84, Y+37", "Prize: X=7870, Y=6450"],
            ["Button A: X+69, Y+23", "Button B: X+27, Y+71", "Prize: X=18641, Y=10279"],
        ]
        self.assertEqual(solution.pt1(input), 480, "Oops")

    # def test_part2(self):
    # input = ""
    # self.assertEqual(solution.pt2(input), "", "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
