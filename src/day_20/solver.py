from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

from src.day_20.models import Range


@dataclass
class Solver(object):
    ips: set[Range]

    @cached_property
    def ordered_ips(self) -> list[Range]:
        return sorted(self.ips)
