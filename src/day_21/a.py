from dataclasses import dataclass
from src.day_21.models import Command, Direction, MovePositions, ReversePositions, RotateBasedOn, RotateDirection, SwapLetters, SwapPositions
from src.day_21.parser import Parser
from src.day_21.solver import Solver

@dataclass
class Day21PartASolver(Solver):
    commands: list[Command]
    start: str

    @property
    def solution(self) -> int:
        arr = list(self.start)
        for command in self.commands:
            match command:
                case SwapPositions(a, b):
                    arr[a], arr[b] = arr[b], arr[a] 
                case SwapLetters(a, b):
                    index_a = arr.index(a)
                    index_b = arr.index(b)
                    arr[index_a], arr[index_b] = arr[index_b], arr[index_a] 
                case RotateDirection(direction, amt):
                    to_rotate = amt if direction == Direction.RIGHT else -amt
                    arr = [arr[(i - to_rotate) % len(arr)] for i in range(len(arr))]
                case RotateBasedOn(letter):
                    to_rotate = arr.index(letter)
                    if to_rotate >= 4:
                        to_rotate += 2
                    else:
                        to_rotate += 1
                    arr = [arr[(i - to_rotate) % len(arr)] for i in range(len(arr))]
                case ReversePositions(a, b):
                    assert a < b
                    arr = arr[:a] + arr[a:b+1][::-1] + arr[b+1:]
                case MovePositions(a, b):
                    letter_a = arr[a]
                    arr = arr[:a] + arr[a+1:]
                    arr = arr[:b] + [letter_a] + arr[b:]

        return "".join(arr)


def solve(input: str, start = "abcdefgh") -> int:
    commands = Parser.parse(input)
    solver = Day21PartASolver(commands=commands, start=start)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_21/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
