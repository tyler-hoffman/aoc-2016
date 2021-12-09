from dataclasses import dataclass
from enum import Enum
from typing import List, Set

class Category(Enum):
    Microchip = 1
    Generator = 2

@dataclass(frozen=True)
class Thing(object):
    category: Category
    element: str

@dataclass
class Floor(object):
    things: Set[Thing]

@dataclass
class State(object):
    floors: List[Floor]
    current_floor: int = 0

