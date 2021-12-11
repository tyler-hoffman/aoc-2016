from dataclasses import dataclass
from src.day_11.models import State
from src.day_11.parser import Parser
from src.day_11.solver import Solver

infinity = float("inf")


@dataclass
class Day11PartBSolver(Solver):
    @property
    def solution(self) -> int:
        return min(self.determine_victory_times())

    def determine_victory_times(self) -> set[int]:
        state = self.start_state
        min_depth_for_state: dict[int, int] = dict()
        discovered_victory_times: set[int] = set()

        self.visit_state_and_progress(
            state, min_depth_for_state, discovered_victory_times
        )

        return discovered_victory_times

    def visit_state_and_progress(
        self,
        state: State,
        min_depth_for_state: dict[int, int],
        discovered_victory_times: set[int],
        depth: int = 0,
    ) -> None:
        if state.is_victory:
            discovered_victory_times.add(depth)
        elif not state.is_valid:
            return
        elif depth < min_depth_for_state.get(hash(state.core_state), infinity):
            min_depth_for_state[hash(state.core_state)] = depth
            for direction in state.valid_elevator_directions:
                for (
                    to_move
                ) in state.current_floor.elements_you_could_move_if_you_wanted:
                    moves_both_of_an_element_down = all([
                        direction == -1,
                        len(to_move) == 2,
                        # len(set([x.element for x in to_move])) == 1,
                    ])
                    moves_down_for_nothing = direction == -1 and all([floor.is_empty for floor in state.floors[:state.current_floor_index]])
                    # moves_down_for_nothing = all([
                    #     direction == -1,
                    #     len(to_move) == 1,
                    # #     all([index >= state.current_floor_index for index in state.floors_for_element(list(to_move)[0].element)])
                    #     not any([floor.contains_element(list(to_move)[0].element) for floor in state.floors[:state.current_floor_index]])
                    # ])
                    if any([
                        moves_both_of_an_element_down,
                        moves_down_for_nothing,
                    ]):
                        continue
                    new_state = state.move_things(to_move, direction)
                    self.visit_state_and_progress(
                        new_state,
                        min_depth_for_state,
                        discovered_victory_times,
                        depth + 1,
                    )


def solve(input: str) -> int:
    state = Parser.parse(input)
    solver = Day11PartBSolver(start_state=state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_11/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
