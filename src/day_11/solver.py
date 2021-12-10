from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import List

from src.day_11.models import Floor, State, Thing


@dataclass
class Solver(ABC):
    start_state: State

    @cached_property
    def all_elements(self) -> set[Thing]:
        return self.start_state.all_elements

    @property
    @abstractmethod
    def solution(self) -> int:
        ...
