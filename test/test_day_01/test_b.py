import unittest

from src.day_01.b import solve


SAMPLE_DATA = "R8, R4, R4, R8"


class TestDay01B(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve(SAMPLE_DATA), 4)

    def test_solution(self):
        with open("src/day_01/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 79)
