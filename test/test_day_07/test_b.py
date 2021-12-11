import unittest

from src.day_07.b import solve


SAMPLE_DATA = """
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cd
"""


class TestDay07B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 3)

    def test_solution(self):
        with open("src/day_07/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 260)
