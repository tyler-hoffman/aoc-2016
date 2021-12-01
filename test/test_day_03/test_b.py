import unittest

from src.day_03.b import solve


class TestDay03B(unittest.TestCase):
    def test_solve(self):
        with open("src/day_03/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 1649)
