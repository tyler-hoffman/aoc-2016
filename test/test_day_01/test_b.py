import unittest

from src.day_01.b import solve


SAMPLE_DATA = "R8, R4, R4, R8"


class TestDay01B(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solve(SAMPLE_DATA), 4)
