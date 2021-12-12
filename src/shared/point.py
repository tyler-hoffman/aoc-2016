from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering
from typing import Any


@total_ordering
@dataclass(frozen=True)
class Point(object):
    x: int
    y: int

    def __add__(self, other: Any) -> Point:
        if isinstance(other, Point):
            return Point(x=self.x + other.x, y=self.y + other.y)
        else:
            raise Exception(f"Point cannot be added with {type(other)}")

    def __lt__(self, other) -> bool:
        if isinstance(other, Point):
            return self.magnitude < other.magnitude
        else:
            raise Exception(f"You can't compare {other} to a Point!")

    def add(self, other: Point) -> Point:
        return Point(x=self.x + other.x, y=self.y + other.y)

    def scale(self, amt: int) -> Point:
        return Point(x=self.x * amt, y=self.y * amt)

    @property
    def magnitude(self) -> int:
        return sum([abs(value) for value in (self.x, self.y)])

    @property
    def magnitude(self) -> int:
        return abs(self.x) + abs(self.y)
