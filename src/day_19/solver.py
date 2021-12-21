from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from functools import cached_property
from typing import Optional


@dataclass
class Solver(ABC):
    elf_count: int

    @cached_property
    def circularly_linked_list(self) -> Link:
        first_link = Link(value=0)
        current_link = first_link
        for i in range(1, self.elf_count):
            new_link = Link(value=i)
            current_link.next = new_link
            current_link = new_link
        current_link.next = first_link
        return first_link


@dataclass
class Link(object):
    value: int
    next: Optional[Link] = None
