import unittest

from src.day_12.b import solve


class TestDay12B(unittest.TestCase):
    def test_optimization_works_for_part_a(self):
        self.assertEqual(solve(do_setup=False), 318007)

    def test_solution(self):
        self.assertEqual(solve(), 9227661)
