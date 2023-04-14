import unittest

from src.day_23.a import solve

SAMPLE_DATA = """
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
"""


class TestDay23A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 3)

    def test_solution(self):
        with open("src/day_23/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 11004)
