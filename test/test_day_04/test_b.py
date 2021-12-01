import unittest

from src.day_04.b import solve


class TestDay04B(unittest.TestCase):
    def test_solve(self):
        with open("src/day_04/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 984)
