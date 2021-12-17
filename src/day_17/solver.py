from abc import ABC
from dataclasses import dataclass, field
from functools import cache, cached_property, total_ordering
from hashlib import md5
from queue import PriorityQueue
from typing import Any, Iterator
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


@dataclass
class Solver(ABC):
    passcode: str
    to_explore: PriorityQueue[State] = field(default_factory=PriorityQueue)
    queue_size: int = 0

    def get_paths(self) -> Iterator[str]:
        self.add_to_queue(State(position=Point(x=0, y=0), path=""))

        while self.queue_size:
            state = self.get_from_queue()
            if state.done:
                yield state.path
            else:
                for door in self.open_doors(state):
                    move = self.directions[door]
                    self.to_explore.put(State(position=state.position + move, path=state.path + door))
                    self.queue_size += 1
        # raise StopIteration()

    def add_to_queue(self, state: State) -> None:
        self.to_explore.put(state)
        self.queue_size += 1

    def get_from_queue(self) -> State:
        self.queue_size -= 1
        return self.to_explore.get()

    def open_doors(self, state: State) -> list[str]:
        up, down, left, right = self.hash(state)[:4]
        output = list[str]()
        if self.is_open(up) and state.position.y > 0:
            output.append("U")
        if self.is_open(down) and state.position.y < 3:
            output.append("D")
        if self.is_open(left) and state.position.x > 0:
            output.append("L")
        if self.is_open(right) and state.position.x < 3:
            output.append("R")
        return output

    def hash(self, state: State) -> str:
        to_hash = self.passcode + state.path
        hashed = md5(to_hash.encode())
        return hashed.hexdigest()

    def is_done(self, state: State) -> bool:
        return state.position == self.end

    @classmethod
    @property
    @cache
    def directions(cls) -> dict[str, Point]:
        return {
            'U': Point(x=0, y=-1),
            'D': Point(x=0, y=1),
            'R': Point(x=1, y=0),
            'L': Point(x=-1, y=0),
        }

    @staticmethod
    def is_open(char: str) -> bool:
        return char in "bcdef"
