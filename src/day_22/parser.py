import re
from typing import List, Mapping
from src.day_22.models import Node
from src.shared.point import Point


class Parser:
    line_pattern = re.compile(r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T")

    @classmethod
    def parse(cls, input: str) -> Mapping[Point, Node]:
        lines = input.splitlines()[2:]
        nodes  = {cls.parse_line(line) for line in lines}
        return {n.coords: n for n in nodes}

    @classmethod
    def parse_line(cls, line: str) -> Node:
        match = cls.line_pattern.search(line)
        assert match is not None

        x, y, size, used, avail = (int(match.group(i)) for i in range(1, 6))
        node = Node(
            coords=Point(x, y),
            size=size,
            used=used,
        )
        assert node.avail == avail

        return node

