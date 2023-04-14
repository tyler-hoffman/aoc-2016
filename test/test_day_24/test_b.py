import unittest

from src.day_24.b import solve


class TestDay24A(unittest.TestCase):
    def test_solution(self):
        with open("src/day_24/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 720)
