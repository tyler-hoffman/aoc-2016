import unittest

from .sample_data import SAMPLE_DATA
from src.day_11.a import solve


class TestDay11A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 11)

    def test_solution(self):
        with open("src/day_11/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 37)
