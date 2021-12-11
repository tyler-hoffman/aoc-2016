from dataclasses import dataclass
from itertools import product

from src.day_11.models import Category, Floor, State, Thing
from src.day_11.parser import Parser
from src.day_11.solver import Solver


@dataclass
class Day11PartBSolver(Solver):
    @property
    def solution(self) -> int:
        state_with_more_stuff = self.add_extra_stuff(self.start_state)
        return self.determine_victory_time(state_with_more_stuff)

    def add_extra_stuff(self, state: State) -> State:
        extra_stuff = [
            Thing(category=c, element=e)
            for c, e in product(
                [Category.Generator, Category.Microchip], ["elerium", "dilithiu"]
            )
        ]
        first_floor_things = set([*state.floors[0].things.copy(), *extra_stuff])

        return State(
            floors=tuple([Floor(things=first_floor_things), *state.floors[1:]])
        )


def solve(input: str) -> int:
    state = Parser.parse(input)
    solver = Day11PartBSolver(state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_11/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
