from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional



@dataclass
class Entity(object):
    id: int

@dataclass
class Bot(Entity):
    give_low: Bot | Output = None
    give_high: Bot | Output = None
    start_values: List[int] = field(default_factory=list)
    values: List[int] = field(default_factory=list)

    @property
    def ready_to_give(self) -> bool:
        return len(self.values) == 2

@dataclass
class Output(Entity):
    values: List[int] = field(default_factory=list)

class Instruction(object):
    pass

@dataclass
class ValueGoesToBot(Instruction):
    bot: Bot
    value: int

@dataclass
class BotGivesValue(Instruction):
    giver: Bot
    low: Entity
    high: Entity
