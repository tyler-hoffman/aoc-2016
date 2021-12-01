import dataclasses
import enum
import re

from typing import Iterator, List

from src.shared.point import Point


class Turn(enum.Enum):
    Left = "LEFT"
    Right = "RIGHT"


DIRECTIONS = [
    Point(0, 1),
    Point(1, 0),
    Point(0, -1),
    Point(-1, 0),
]


@dataclasses.dataclass
class Instruction(object):
    turn: Turn
    steps: int


def follow_instructions(instructions: List[Instruction]) -> Iterator[Point]:
    point = Point(x=0, y=0)
    direction_index = 0

    yield point

    for instruction in instructions:
        if instruction.turn == Turn.Left:
            direction_index = (direction_index + 3) % len(DIRECTIONS)
        elif instruction.turn == Turn.Right:
            direction_index = (direction_index + 1) % len(DIRECTIONS)
        else:
            raise Exception(f"Invalid turn {instruction.turn}")

        direction = DIRECTIONS[direction_index]
        point = point.add(direction.scale(instruction.steps))

        yield point


def parse_part(input: str) -> Instruction:
    match = re.search("(R|L)(\\d+)", input)
    assert match is not None

    turn: Turn
    turn_string = match.group(1)
    if turn_string == "L":
        turn = Turn.Left
    elif turn_string == "R":
        turn = Turn.Right
    else:
        raise Exception(f"Unexpected turn value: {turn_string}")

    return Instruction(turn=turn, steps=int(match.group(2)))


def parse(input: str) -> List[Instruction]:
    return [parse_part(part) for part in input.split(", ")]
