import unittest

from src.day_22.a import solve


class TestDay22A(unittest.TestCase):
    def test_solution(self):
        with open("src/day_22/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 872)
