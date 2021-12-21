from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class Solver(ABC):
    @property
    @abstractmethod
    def solution(self) -> int:
        ...

@dataclass
class Link(object):
    value: int
    next: Optional[Link] = None
