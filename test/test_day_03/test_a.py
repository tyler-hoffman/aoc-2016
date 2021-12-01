import unittest

from src.day_03.a import solve


class TestDay03A(unittest.TestCase):
    def test_solution(self):
        with open("src/day_03/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 917)
