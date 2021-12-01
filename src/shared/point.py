import dataclasses
from __future__ import annotations

@dataclasses.dataclass
class Point(object):
    x: int
    y: int

    def add(self, other: Point) -> Point:
        return Point(x=self.x + other.x, y=self.y + other.y)
