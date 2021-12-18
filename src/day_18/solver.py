from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from os import stat
from typing import Iterator


@dataclass
class Solver(ABC):
    first_row: list[bool]
    row_count: int

    def rows(self) -> Iterator[list[bool]]:
        row = self.first_row

        while True:
            yield row
            row = self.next_row(row)

    def next_row(self, prev: list[bool]) -> list[bool]:
        return [self.next_value(prev, i) for i in range(len(prev))]

    def next_value(self, prev: list[bool], index: int) -> bool:
        left = index == 0 or prev[index - 1]
        center = prev[index]
        right = index == self.row_len - 1 or prev[index + 1]

        return not any(
            [
                [left, center, right] == [True, True, False],
                [left, center, right] == [False, True, True],
                [left, center, right] == [True, False, False],
                [left, center, right] == [False, False, True],
            ]
        )

    @cached_property
    def row_len(self) -> int:
        return len(self.first_row)

    @staticmethod
    def row_safe_count(row: list[bool]) -> int:
        return len([x for x in row if x])
