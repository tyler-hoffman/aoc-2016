import unittest

from .sample_data import SAMPLE_DATA
from src.day_14.b import solve


class TestDay14B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 22551)

    def test_solution(self):
        with open("src/day_14/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 22045)
