from __future__ import annotations
from dataclasses import dataclass
from src.shared.point import Point


@dataclass
class Node:
    coords: Point
    size: int
    used: int

    @property
    def avail(self) -> int:
        return self.size - self.used

    @property
    def empty(self) -> bool:
        return self.used == 0

    def __hash__(self) -> int:
        return hash(self.coords)

    def with_used(self, amt: int) -> Node:
        return Node(self.coords, self.size, amt)

