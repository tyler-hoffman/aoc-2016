import unittest

from .sample_data import SAMPLE_DATA
from src.day_11.b import solve


class TestDay11B(unittest.TestCase):
    def test_solve(self):
        with open("src/day_11/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 61)
