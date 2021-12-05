from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Solver(ABC):
    @property
    @abstractmethod
    def solution(self) -> int:
        ...
