from dataclasses import dataclass
from queue import PriorityQueue
from typing import Iterator, Tuple

from src.day_11.models import CoreState, State
from src.day_11.parser import Parser
from src.day_11.solver import Solver

infinity = float("inf")


@dataclass
class Day11PartASolver(Solver):
    @property
    def solution(self) -> int:
        return self.determine_victory_time()

    def determine_victory_time(self) -> int:
        basically_covered_stuff = set[CoreState]()
        to_check = PriorityQueue[Tuple[int, int, State]]()
        to_check.put((self.start_state.optimistic_steps_to_finish, -self.start_state.steps, self.start_state))

        while not to_check.empty():
            _, _, state = to_check.get()
            if state.core_state in basically_covered_stuff:
                continue

            if state.is_victory:
                return state.steps
            else:
                basically_covered_stuff.add(state.core_state)
                for next_state in self.potential_next_steps_for_state(state):
                    to_check.put((next_state.optimistic_steps_to_finish, -next_state.steps, next_state))

        assert False, "We should have returned a solution by now"

    def potential_next_steps_for_state(self, state: State) -> Iterator[State]:
        for direction in state.valid_elevator_directions:
            for to_move in state.current_floor.elements_you_could_move_if_you_wanted:
                if (next_state := state.move_things(to_move, direction)).is_valid: 
                    yield next_state


def solve(input: str) -> int:
    state = Parser.parse(input)
    solver = Day11PartASolver(start_state=state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_11/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
