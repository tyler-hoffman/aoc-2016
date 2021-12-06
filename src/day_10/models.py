from __future__ import annotations
from abc import ABC
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Entity(ABC):

    def receive_value(self, value: int) -> None:
        ...

@dataclass
class Bot(object):
    id: int
    give_low: Bot | Output = None
    give_high: Bot | Output = None
    start_values: List[int] = field(default_factory=list)
    values: List[int] = field(default_factory=list)

    @property
    def ready_to_give(self) -> bool:
        return len(self.values) == 2

    def receive_value(self, value: int) -> None:
        self.values.append(value)

@dataclass
class Output(Entity):
    id: int
    value: int = None

    def receive_value(self, value: int) -> None:
        self.value = value
