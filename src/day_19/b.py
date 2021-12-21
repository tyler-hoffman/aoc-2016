from src.day_19.parser import Parser
from src.day_19.solver import Solver


class Day19PartBSolver(Solver):
    @property
    def solution(self) -> int:
        jump_after_steal = bool(self.elf_count % 2)
        before_stealee = self.circularly_linked_list
        for _ in range(self.elf_count // 2 - 1):
            before_stealee = before_stealee.next

        while before_stealee.next != before_stealee:
            before_stealee.next = before_stealee.next.next
            if jump_after_steal:
                before_stealee = before_stealee.next
            jump_after_steal = not jump_after_steal
        return before_stealee.value + 1


def solve(input: str) -> int:
    elf_count = Parser.parse(input)
    solver = Day19PartBSolver(elf_count=elf_count)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_19/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
