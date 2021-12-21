import unittest

from src.day_19.b import solve


class TestDay19B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("5"), 2)

    def test_solution(self):
        with open("src/day_19/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 1417887)
