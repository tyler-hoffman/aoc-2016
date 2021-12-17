from dataclasses import dataclass
from functools import cache, cached_property, total_ordering
from typing import Any

from src.shared.point import Point


@total_ordering
@dataclass(frozen=True)
class State(object):
    position: Point
    path: str

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, State):
            return self.optimistic_best_length < other.optimistic_best_length
        else:
            raise Exception(f"{other} can't be compared to State")

    @cached_property
    def optimistic_best_length(self) -> int:
        dist_to_end = self.position.manhattan_dist(self.end)
        return len(self.path) + dist_to_end

    @cached_property
    def done(self) -> bool:
        return self.position == self.end

    @classmethod
    @property
    @cache
    def end(cls) -> Point:
        return Point(3, 3)
