from dataclasses import dataclass
from functools import cached_property
from typing import Mapping
from src.day_21.models import (
    Command,
    Direction,
    MovePositions,
    ReversePositions,
    RotateBasedOn,
    RotateDirection,
    SwapLetters,
    SwapPositions,
)
from src.day_21.parser import Parser
from src.day_21.solver import Solver


@dataclass
class Day21PartBSolver(Solver):
    commands: list[Command]
    start: str

    @property
    def solution(self) -> int:
        arr = list(self.start)
        for command in self.commands[::-1]:
            match command:
                case SwapPositions(a, b):
                    arr[a], arr[b] = arr[b], arr[a]
                case SwapLetters(a, b):
                    index_a = arr.index(a)
                    index_b = arr.index(b)
                    arr[index_a], arr[index_b] = arr[index_b], arr[index_a]
                case RotateDirection(direction, amt):
                    to_rotate = -amt if direction == Direction.RIGHT else amt
                    arr = [arr[(i - to_rotate) % len(arr)] for i in range(len(arr))]
                case RotateBasedOn(letter):
                    index_after = arr.index(letter)
                    index_before = self.unrotate_based_on_char_map[index_after]
                    to_rotate = index_after - index_before
                    arr = [arr[(i + to_rotate) % len(arr)] for i in range(len(arr))]
                case ReversePositions(a, b):
                    assert a < b
                    arr = arr[:a] + arr[a : b + 1][::-1] + arr[b + 1 :]
                case MovePositions(a, b):
                    letter_b = arr[b]
                    arr = arr[:b] + arr[b + 1 :]
                    arr = arr[:a] + [letter_b] + arr[a:]

        return "".join(arr)

    @cached_property
    def rotate_based_on_char_map(self) -> Mapping[int, int]:
        def get_rotation_amount(char_index: int) -> int:
            extra = 2 if char_index >= 4 else 1
            new_pos = char_index * 2 + extra
            return new_pos % len(self.start)

        return {
            before: get_rotation_amount(before) for before in range(len(self.start))
        }

    @cached_property
    def unrotate_based_on_char_map(self) -> Mapping[int, int]:
        return {end: start for start, end in self.rotate_based_on_char_map.items()}


def solve(input: str, start="fbgdceah") -> int:
    commands = Parser.parse(input)
    solver = Day21PartBSolver(commands=commands, start=start)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_21/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
