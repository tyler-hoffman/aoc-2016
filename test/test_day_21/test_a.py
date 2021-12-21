import unittest

from .sample_data import SAMPLE_DATA
from src.day_21.a import solve


class TestDay21A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), "decab")
