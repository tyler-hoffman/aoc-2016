import unittest

from src.day_05.a import solve


class TestDay05A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("abc"), "18f47a30")

    def test_solution(self):
        self.assertEqual(solve("ugkcyxxp"), "d4cd2ee1")
