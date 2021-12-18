from dataclasses import dataclass
from functools import cached_property
from math import ceil
from src.day_19.parser import Parser
from src.day_19.solver import Link, Solver


@dataclass
class Day19PartBSolver(Solver):
    elf_count: int

    @property
    def solution(self) -> int:
        link = self.circularly_linked_list
        while link.next != link:
            link.next = link.next.next
            link = link.next
        return link.value

    @cached_property
    def circularly_linked_list(self) -> Link:
        half = ceil(self.elf_count / 2)
        first_link = Link(value = 1)
        current_link = first_link
        for i in range(2, self.elf_count + 1):
            new_link = Link(value=i, prev=current_link)
            current_link.next=new_link
            current_link=new_link
        current_link.next=first_link
        first_link.prev = current_link
        return first_link



def solve(input: str) -> int:
    elf_count = Parser.parse(input)
    solver = Day19PartBSolver(elf_count=elf_count)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_19/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
