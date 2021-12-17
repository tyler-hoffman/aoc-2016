import unittest

from src.day_18.b import solve


class TestDay18B(unittest.TestCase):
    def test_solution(self):
        with open("src/day_18/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input, 400000), 1957)
