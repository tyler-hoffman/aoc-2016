from __future__ import annotations
import enum
from typing import List
from src.shared.point import Point


class Direction(enum.Enum):
    Up = "UP"
    Down = "DOWN"
    Left = "LEFT"
    Right = "RIGHT"

    @classmethod
    def from_string(cls, s: str) -> Direction:
        if s == "U":
            return Direction.Up
        elif s == "D":
            return Direction.Down
        elif s == "L":
            return Direction.Left
        elif s == "R":
            return Direction.Right
        else:
            raise Exception(f"Unexpected string {s}")


NUMBERS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def move(pos: Point, directions: List[Direction]) -> Point:
    for direction in directions:
        if direction == Direction.Up:
            pos = Point(x=pos.x, y=max(0, pos.y - 1))
        elif direction == Direction.Down:
            pos = Point(x=pos.x, y=min(2, pos.y + 1))
        elif direction == Direction.Left:
            pos = Point(x=max(0, pos.x - 1), y=pos.y)
        elif direction == Direction.Right:
            pos = Point(x=min(2, pos.x + 1), y=pos.y)
    return pos


def number_at_point(point: Point) -> int:
    return NUMBERS[point.y][point.x]


def parse(input: str) -> List[List[Direction]]:
    output: List[List[Direction]] = []

    for line in input.strip().splitlines():
        output.append([Direction.from_string(char) for char in line])

    return output
