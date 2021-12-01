from __future__ import annotations

import dataclasses


@dataclasses.dataclass(frozen=True)
class Point(object):
    x: int
    y: int

    def add(self, other: Point) -> Point:
        return Point(x=self.x + other.x, y=self.y + other.y)

    def scale(self, amt: int) -> Point:
        return Point(x=self.x * amt, y=self.y * amt)

    @property
    def magnitude(self) -> int:
        return abs(self.x) + abs(self.y)
