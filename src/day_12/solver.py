from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.shared.machine import Instruction


@dataclass
class Solver(ABC):
    instructions: list[Instruction]

    @property
    @abstractmethod
    def solution(self) -> int:
        ...
