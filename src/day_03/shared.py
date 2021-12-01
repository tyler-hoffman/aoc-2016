import dataclasses
import re
from typing import List


@dataclasses.dataclass
class Triangle(object):
    a: int
    b: int
    c: int

    @property
    def is_valid(self) -> bool:
        half_length = sum([self.a, self.b, self.c]) / 2

        return all([x < half_length for x in [self.a, self.b, self.c]])


def parse_triangle(line: str) -> Triangle:
    match = re.search("(\d+)\s+(\d+)\s+(\d+)", line)
    assert match is not None

    return Triangle(a=int(match.group(1)), b=int(match.group(2)), c=int(match.group(3)))


def parse(input: str) -> List[Triangle]:
    lines = [line for line in input.splitlines() if line]
    return [parse_triangle(line) for line in lines]
