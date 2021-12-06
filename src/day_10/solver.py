from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterator, List, Tuple

from src.day_10.models import Bot, Entity, Output


@dataclass
class Distribution(object):
    giver: Bot
    given: Tuple[int, int]
    receivers: Tuple[Entity, Entity]


@dataclass
class Solver(ABC):
    bots: List[Bot]
    outputs: List[Output]

    @property
    @abstractmethod
    def solution(self) -> int:
        ...

    def distribute_chips(self) -> Iterator[Distribution]:
        self.setup()

        while bots_ready_to_give := [bot for bot in self.bots if bot.ready_to_give]:
            assert len(bots_ready_to_give) > 0
            for bot in bots_ready_to_give:
                low = min(bot.values)
                high = max(bot.values)

                bot.give_low.receive_value(low)
                bot.give_high.receive_value(high)
                bot.values = []

                yield Distribution(
                    giver=bot,
                    given=[low, high],
                    receivers=[bot.give_low, bot.give_high],
                )

    def setup(self) -> None:
        for bot in self.bots:
            bot.values = bot.start_values.copy()
