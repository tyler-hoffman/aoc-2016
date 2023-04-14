from typing import List

from src.day_24.models import Map
from src.shared.point import Point


class Parser(object):
    @staticmethod
    def parse(input: str) -> Map:
        lines = input.strip().splitlines()
        spaces: set[Point] = set()
        nodes: dict[int, Point] = {}
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                point = Point(x, y)
                if char.isnumeric():
                    nodes[int(char)] = point
                    spaces.add(point)
                if char is ".":
                    spaces.add(point)
        return Map(spaces, nodes)
