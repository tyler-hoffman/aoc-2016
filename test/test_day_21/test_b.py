import unittest

from .sample_data import SAMPLE_DATA
from src.day_21.b import solve


class TestDay21B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA, "decab"), "abcde")

    def test_solution(self):
        with open("src/day_21/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), "egcdahbf")
