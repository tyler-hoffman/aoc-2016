import unittest

from src.shared.point import Point

from src.day_13.a import solve
from test.test_day_13.sample_data import SAMPLE_DATA


class TestDay13A(unittest.TestCase):
    def test_solve(self):
        goal = SAMPLE_DATA
        secret = 10
        self.assertEqual(solve(goal=goal, secret=secret), 11)

    def test_solution(self):
        goal = Point(x=31,y=39)
        secret = 1352
        self.assertEqual(solve(goal=goal, secret=secret), 90)
