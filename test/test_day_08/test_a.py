import unittest

from src.day_08.a import solve


SAMPLE_DATA = """
rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
"""


class TestDay08A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA, width=7, height=3), 6)
