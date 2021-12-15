from more_itertools.more import chunked

from dataclasses import dataclass


@dataclass
class Solver(object):
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
            return Solver.checksum(checksum)
        else:
            return checksum

    @staticmethod
    def dragon(stuff: list[str]) -> list[str]:
        return stuff + ["0"] + Solver.flip_it_and_reverse_it(stuff)

    @staticmethod
    def flip_it_and_reverse_it(items: list[str]) -> list[str]:
        return [Solver.flip_bit(bit) for bit in items[::-1]]

    @staticmethod
    def flip_bit(bit: str) -> str:
        match bit:
            case "0":
                return "1"
            case "1":
                return "0"
            case _:
                raise Exception(f"Wat? {bit}")
