import unittest

from src.day_15.b import solve


class TestDay15B(unittest.TestCase):
    def test_solution(self):
        with open("src/day_15/input.txt", "r") as f:
            all_lines = f.read()
            self.assertEqual(solve(all_lines), 3045959)
