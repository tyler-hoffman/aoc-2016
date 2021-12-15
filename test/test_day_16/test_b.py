import unittest

from src.day_16.b import solve


class TestDay16B(unittest.TestCase):
    def test_solve(self):
        with open("src/day_16/input.txt", "r") as f:
            initial_state = f.read()
            self.assertEqual(solve(initial_state), "00011010100010010")
