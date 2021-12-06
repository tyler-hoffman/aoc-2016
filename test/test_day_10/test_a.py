import unittest

from .sample_data import SAMPLE_DATA
from src.day_10.a import solve


class TestDay10A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA, (5, 2)), 2)

    def test_solution(self):
        with open("src/day_10/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input, (61, 17)), 98)
