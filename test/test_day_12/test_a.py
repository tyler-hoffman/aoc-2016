import unittest

from .sample_data import SAMPLE_DATA
from src.day_12.a import solve


class TestDay12A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 42)

    def test_solution(self):
        with open("src/day_12/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 318007)
