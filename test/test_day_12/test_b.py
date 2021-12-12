import unittest

from src.day_12.b import solve


class TestDay12B(unittest.TestCase):
    def test_solve(self):
        with open("src/day_12/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 1)
