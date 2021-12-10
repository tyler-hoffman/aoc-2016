from dataclasses import dataclass, field
from src.day_11.models import State
from src.day_11.parser import Parser
from src.day_11.solver import Solver

infinity = float("inf")

@dataclass
class Day11PartASolver(Solver):
    @property
    def solution(self) -> int:
        return min(self.determine_victory_times())

    def determine_victory_times(self) -> set[int]:
        state = self.start_state
        min_depth_for_state: dict[State, int] = dict()
        discovered_victory_times: set[int] = set()

        self.visit_state_and_progress(
            state, min_depth_for_state, discovered_victory_times
        )

        return discovered_victory_times

    def visit_state_and_progress(
        self,
        state: State,
        min_depth_for_state: dict[State, int],
        discovered_victory_times: set[int],
        depth: int = 0,
    ) -> None:
        if state.is_victory:
            discovered_victory_times.add(depth)
        elif not state.is_valid:
            return
        elif depth < min_depth_for_state.get(state, infinity):
            min_depth_for_state[state] = depth
            for direction in state.valid_elevator_directions:
                for (
                    to_move
                ) in state.current_floor.elements_you_could_move_if_you_wanted:
                    new_state = state.move_things(to_move, direction)
                    self.visit_state_and_progress(
                        new_state,
                        min_depth_for_state,
                        discovered_victory_times,
                        depth + 1,
                    )


def solve(input: str) -> int:
    state = Parser.parse(input)
    solver = Day11PartASolver(start_state=state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_11/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
