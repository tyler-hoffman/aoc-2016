import unittest

from src.day_17.b import solve


class TestDay17B(unittest.TestCase):
    def test_solve(self):
        with open("src/day_17/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 788)
