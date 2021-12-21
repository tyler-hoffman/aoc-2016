from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering


@total_ordering
@dataclass(frozen=True)
class Range(object):
    start: int
    end: int

    def __lt__(self, other: Range) -> bool:
        return self.start < other.start
