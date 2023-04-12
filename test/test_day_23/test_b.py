import unittest

from src.day_23.b import solve


class TestDay23B(unittest.TestCase):
    def test_solution(self):
        with open("src/day_23/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 479007564)
