from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property, total_ordering
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

    def manhattan_dist(self, other: Point) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    @property
    def manhattan_neighbors(self) -> set[Point]:
        return {
            Point(self.x, self.y - 1),
            Point(self.x, self.y + 1),
            Point(self.x - 1, self.y),
            Point(self.x + 1, self.y),
        }

    @cached_property
    def magnitude(self) -> int:
        return abs(self.x) + abs(self.y)
