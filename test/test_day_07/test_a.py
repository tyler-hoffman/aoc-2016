import unittest

from src.day_07.a import solve


SAMPLE_INPUT = """
abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
"""

class TestDay07A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_INPUT), 2)
