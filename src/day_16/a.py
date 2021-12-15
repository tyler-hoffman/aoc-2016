from dataclasses import dataclass

from more_itertools.more import chunked
from src.day_16.solver import Solver


@dataclass
class Day16PartASolver(Solver):
    disk_size: int
    initial_state: str

    @property
    def solution(self) -> str:
        stuff = list(self.initial_state)
        while len(stuff) < self.disk_size:
            stuff = self.dragon(stuff)
        stuff = stuff[: self.disk_size]
        checksum = self.checksum(stuff)
        return "".join(checksum)

    @staticmethod
    def checksum(stuff: list[str]) -> list[str]:
        checksum = ["1" if a == b else "0" for a, b in chunked(stuff, 2)]

        if len(checksum) % 2 == 0:
            return Day16PartASolver.checksum(checksum)
        else:
            return checksum

    @staticmethod
    def dragon(stuff: list[str]) -> list[str]:
        return stuff + ["0"] + Day16PartASolver.flip_it_and_reverse_it(stuff)

    @staticmethod
    def flip_it_and_reverse_it(items: list[str]) -> list[str]:
        return [Day16PartASolver.flip_bit(bit) for bit in items[::-1]]

    @staticmethod
    def flip_bit(bit: str) -> str:
        match bit:
            case "0":
                return "1"
            case "1":
                return "0"
            case _:
                raise Exception(f"Wat? {bit}")


def solve(initial_state: str, disk_size: int = 272) -> int:
    initial_state = initial_state.strip()
    solver = Day16PartASolver(disk_size=disk_size, initial_state=initial_state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_16/input.txt", "r") as f:
        initial_state = f.read()
        print(solve(initial_state))
