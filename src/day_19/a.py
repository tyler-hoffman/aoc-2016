from src.day_19.parser import Parser
from src.day_19.solver import Solver


class Day19PartASolver(Solver):
    @property
    def solution(self) -> int:
        link = self.circularly_linked_list
        while link.next != link:
            link.next = link.next.next
            link = link.next
        return link.value + 1


def solve(input: str) -> int:
    elf_count = Parser.parse(input)
    solver = Day19PartASolver(elf_count=elf_count)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_19/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
