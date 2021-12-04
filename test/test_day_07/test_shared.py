from parameterized import parameterized
import unittest

from src.day_07.shared import IpAddress


class TestDay07IpAddress(unittest.TestCase):
    @parameterized.expand([
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
    ])
    def test_supports_tls(self, value: str, expected):
        ip_address = IpAddress(value)

        self.assertEqual(ip_address.supports_tls, expected)
