from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import List

from src.day_11.models import Floor, State, Thing


@dataclass
class Solver(ABC):
    state: State

    @cached_property
    def all_elements(self) -> set[Thing]:
        output: set[Thing] = set()
        for floor in self.state.floors:
            for thing in floor.things:
                output.add(thing.element)
        return output

    @cached_property
    def elements(self) -> set[str]:
        return set([thing.element for thing in self.f])

    @cached_property
    def floor_count(self) -> int:
        return len(self.floors)

    @cached_property
    def target_floor(self) -> int:
        return self.floor_count - 1

    @property
    @abstractmethod
    def solution(self) -> int:
        ...
