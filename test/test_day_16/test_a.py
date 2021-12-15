import unittest

from .sample_data import SAMPLE_DATA
from src.day_16.a import solve


class TestDay16A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1)
