from __future__ import annotations
from dataclasses import dataclass
import dataclasses
import enum
from typing import Dict, List
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


@dataclasses.dataclass
class Keypad(object):
    values: Dict[Point, str]

    def position_of(self, look_for: str) -> Point:
        for point, value in self.values.items():
            if value == look_for:
                return point
        assert False, f"Value {look_for} not found"

    def move(self, pos: Point, directions: List[Direction]) -> Point:
        for direction in directions:
            new_pos: Point
            if direction == Direction.Up:
                new_pos = Point(x=pos.x, y=pos.y - 1)
            elif direction == Direction.Down:
                new_pos = Point(x=pos.x, y=pos.y + 1)
            elif direction == Direction.Left:
                new_pos = Point(x=pos.x - 1, y=pos.y)
            elif direction == Direction.Right:
                new_pos = Point(x=pos.x + 1, y=pos.y)

            if new_pos in self.values:
                pos = new_pos

        return pos

    def char_at_point(self, point: Point) -> str:
        output = self.values.get(point)
        assert output is not None, f"Invalid point {point}"

        return output

    @classmethod
    def from_string(cls, input: str) -> Keypad:
        values = dict[Point, str]()

        for y, line in enumerate([line for line in input.splitlines() if line]):
            for i, char in enumerate(line):
                # skip every other space since it's just formatting
                if i % 2 > 0:
                    pass
                elif char != " ":
                    values[Point(x=i // 2, y=y)] = char

        return Keypad(values=values)


def parse(input: str) -> List[List[Direction]]:
    output: List[List[Direction]] = []

    for line in input.strip().splitlines():
        output.append([Direction.from_string(char) for char in line])

    return output
