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
        input = open("src/day_02/input.txt", "r").read()
        self.assertEqual(solve(input), "98575")
