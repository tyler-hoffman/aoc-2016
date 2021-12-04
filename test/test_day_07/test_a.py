import unittest

from src.day_07.a import solve


class TestDay07A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(input), 1)
