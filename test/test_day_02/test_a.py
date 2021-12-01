import unittest

from src.day_02.a import solve


SAMPLE_DATA = """
ULL
RRDDD
LURDL
UUUUD
"""


class TestDay02A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), "1985")

    def test_solution(self):
        with open("src/day_02/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), "98575")
