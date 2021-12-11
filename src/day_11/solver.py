from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from queue import PriorityQueue
from typing import Iterator, Tuple

from src.day_11.models import CoreState, State, Thing


@dataclass
class Solver(ABC):
    start_state: State

    @property
    @abstractmethod
    def solution(self) -> int:
        ...

    def determine_victory_time(self, state: State) -> int:
        basically_covered_stuff = set[CoreState]()
        to_check = PriorityQueue[Tuple[int, int, State]]()
        to_check.put((state.optimistic_steps_to_finish, -state.steps, state))

        while not to_check.empty():
            _, _, state = to_check.get()
            if state.core_state in basically_covered_stuff:
                continue
            elif state.is_victory:
                return state.steps
            else:
                basically_covered_stuff.add(state.core_state)
                for next_state in self.potential_next_steps_for_state(state):
                    to_check.put(
                        (
                            next_state.optimistic_steps_to_finish,
                            -next_state.steps,
                            next_state,
                        )
                    )
        assert False, "We should have returned a solution by now"

    def potential_next_steps_for_state(self, state: State) -> Iterator[State]:
        for direction in state.valid_elevator_directions:
            for to_move in state.current_floor.elements_you_could_move_if_you_wanted:
                if (next_state := state.move_things(to_move, direction)).is_valid:
                    yield next_state
