import unittest

from src.day_10.b import solve
from test.test_day_10.sample_data import SAMPLE_DATA


class TestDay10B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 2 * 3 * 5)

    def test_solution(self):
        with open("src/day_10/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 4042)
