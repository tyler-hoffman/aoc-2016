from dataclasses import dataclass

from src.day_15.models import Disk


@dataclass
class Solver(object):
    disks: list[Disk]

    @property
    def solution(self) -> int:
        t = 0
        multiplier = 1
        for disk in self.disks:
            while (t + disk.superimposed_start) % disk.positions:
                t += multiplier
            multiplier *= disk.positions
        return t
