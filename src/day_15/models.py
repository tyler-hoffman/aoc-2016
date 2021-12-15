from dataclasses import dataclass
from functools import cached_property


@dataclass
class Disk(object):
    positions: int
    start: int
    depth: int

    @cached_property
    def superimposed_start(self) -> int:
        return (self.start + self.depth) % self.positions
