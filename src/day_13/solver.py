from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import cache, cached_property
from enum import Enum
from queue import PriorityQueue
from typing import Iterator

from src.shared.point import Point


class Entity(Enum):
    Wall = 1
    Space = 2


@dataclass
class Solver(ABC):
    secret: int

    @property
    @abstractmethod
    def solution(self) -> int:
        ...

    @cached_property
    def board(self) -> Board:
        return Board(secret=self.secret)


@dataclass
class CellData(object):
    point: Point
    steps: int


@dataclass
class Board(object):
    secret: int
    to_check: PriorityQueue[tuple[int, Point]] = field(default_factory=PriorityQueue)
    marked: set[Point] = field(default_factory=set)

    def discover(self) -> Iterator[CellData]:
        start = Point(1, 1)
        self.marked.add(start)
        self.to_check.put((0, start))

        while True:
            steps, point = self.to_check.get()
            yield CellData(point=point, steps=steps)
            for neighbor in self.get_neighbors(point):
                if neighbor not in self.marked:
                    self.marked.add(neighbor)
                    self.to_check.put((steps + 1, neighbor))

    def get_neighbors(self, point: Point) -> list[Point]:
        potentials = [point + move for move in self.moves()]
        return [x for x in potentials if self.is_valid(x)]

    def is_valid(self, point: Point) -> bool:
        return all(
            [
                point.x >= 0,
                point.y >= 0,
                self.point_to_entity(point) != Entity.Wall,
            ]
        )

    def point_to_entity(self, point: Point) -> Entity:
        x, y = point.x, point.y
        number = x * x + 3 * x + 2 * x * y + y + y * y + self.secret

        return self.int_to_entity(number)

    @staticmethod
    def int_to_entity(x: int) -> Entity:
        bits = bin(x)[2:]
        ones = len([bit for bit in bits if bit == "1"])

        return Entity.Space if ones % 2 == 0 else Entity.Wall

    @staticmethod
    @cache
    def moves() -> list[Point]:
        return [
            Point(x=0, y=-1),
            Point(x=0, y=1),
            Point(x=-1, y=0),
            Point(x=1, y=0),
        ]
