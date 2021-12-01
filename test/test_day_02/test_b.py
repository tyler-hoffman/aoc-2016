import unittest

from src.day_02.b import solve

SAMPLE_DATA = """
ULL
RRDDD
LURDL
UUUUD
"""

class TestDay02B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), "5DB3")

    def test_solution(self):
        with open("src/day_02/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), "CD8D4")
