from functools import cache
import re
from typing import List

from src.day_15.models import Disk


class Parser(object):
    @classmethod
    def parse(cls, all_lines: str) -> List[Disk]:
        return [cls.parse_disk(line) for line in all_lines.strip().splitlines()]

    @classmethod
    def parse_disk(cls, line: str) -> Disk:
       depth, positions, _, start  = [int(x) for x in re.findall(r"\d+", line)]
       return Disk(positions=positions, start=start, depth=depth)

    @staticmethod
    @cache
    def disk_regex() -> re.Pattern:
        return re.compile(r".* #(\d+);.*time\=(\d+);.* (\d+).")
