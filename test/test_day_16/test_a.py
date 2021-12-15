import unittest

from src.day_16.a import solve


class TestDay16A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(disk_size=20, initial_state="10000"), "01100")

    def test_solution(self):
        with open("src/day_16/input.txt", "r") as f:
            initial_state = f.read()
            self.assertEqual(solve(initial_state), "00000100100001100")
