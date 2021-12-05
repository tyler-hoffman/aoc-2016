import unittest
from parameterized import parameterized

from src.day_09.a import encrypt


class TestDay09A(unittest.TestCase):
    @parameterized.expand(
        [
            ("ADVENT", "ADVENT"),
            ("A(1x5)BC", "ABBBBBC"),
            ("(3x3)XYZ", "XYZXYZXYZ"),
            ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG"),
            ("(6x1)(1x3)A", "(1x3)A"),
            ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY"),
        ]
    )
    def test_solve(self, input: str, expected: str):
        self.assertEqual(encrypt(input), expected)
