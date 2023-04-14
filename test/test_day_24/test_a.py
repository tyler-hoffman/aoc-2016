import unittest

from .sample_data import SAMPLE_DATA
from src.day_24.a import solve


class TestDay24A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 14)

    def test_solution(self):
        with open("src/day_24/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 470)
