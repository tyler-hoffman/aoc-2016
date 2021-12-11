from __future__ import annotations
from dataclasses import dataclass
from functools import cache, cached_property, total_ordering
from itertools import combinations
from enum import Enum
from typing import Iterable, Iterator, List, Tuple


class Category(Enum):
    Microchip = 1
    Generator = 2


@dataclass(frozen=True)
class CoreState(object):
    floors: Tuple[CoreFloor, CoreFloor, CoreFloor, CoreFloor]
    current_floor_index: int
    steps: int


@dataclass(frozen=True)
class CoreFloor(object):
    lone_generators: int
    lone_microchips: int
    pairs: int


@dataclass(frozen=True)
class Thing(object):
    category: Category
    element: str

    def __repr__(self) -> str:
        first_char = self.element[0].upper()
        match self.category:
            case Category.Microchip:
                return f"{first_char}M"
            case Category.Generator:
                return f"{first_char}G"


@dataclass(frozen=True)
class Floor(object):
    things: frozenset[Thing]

    def __repr__(self) -> str:
        return f"{[f'{thing}' for thing in self.things]}"

    @property
    def elements_you_could_move_if_you_wanted(self) -> Iterable[set[Thing]]:
        for thing in self.things:
            yield set([thing])
        for pair in combinations(self.things, 2):
            yield set(pair)

    @cached_property
    def is_valid(self) -> bool:
        return all(
            [self._element_is_safe(element) for element in self.microchip_elements]
        )

    @cached_property
    def is_empty(self) -> bool:
        return len(self.things) == 0

    @cached_property
    def generator_elements(self) -> frozenset[str]:
        return self._get_elements_by_category(Category.Generator)

    @cached_property
    def microchip_elements(self) -> frozenset[str]:
        return self._get_elements_by_category(Category.Microchip)

    def _element_is_safe(self, element: str) -> bool:
        return element in self.generator_elements or not self.generator_elements

    def _get_elements_by_category(self, category: Category) -> frozenset[str]:
        return frozenset([x.element for x in self.things if x.category == category])

    @cached_property
    def core_floor(self) -> CoreFloor:
        generator_elements = {
            thing.element
            for thing in self.things
            if thing.category == Category.Generator
        }
        microchip_elements = {
            thing.element
            for thing in self.things
            if thing.category == Category.Microchip
        }
        return CoreFloor(
            lone_generators=len(generator_elements - microchip_elements),
            lone_microchips=len(microchip_elements - generator_elements),
            pairs=len(generator_elements.intersection(microchip_elements)),
        )


@total_ordering
@dataclass(frozen=True)
class State(object):
    floors: Tuple[Floor, Floor, Floor, Floor]
    steps: int = 0
    current_floor_index: int = 0

    def __lt__(self, other) -> bool:
        if isinstance(other, State):
            return self.optimistic_steps_to_finish < other.optimistic_steps_to_finish
        else:
            return False

    @cached_property
    def optimistic_steps_to_finish(self) -> int:
        return self.steps + self.optimistic_steps_remaining

    @cached_property
    def optimistic_steps_remaining(self) -> int:
        if self.is_victory:
            return 0

        current_index = self.current_floor_index
        if (item_count := len(self.current_floor.things)) > 1:
            output = self.cost_to_clear_floor(
                current_index, item_count - 1, current_index
            )
            remaining_floors: tuple[int, Floor] = [
                (i, floor)
                for i, floor in enumerate(self.floors[:3])
                if i is not current_index and not floor.is_empty
            ]
        else:
            output = self.cost_to_clear_floor(
                self.lowest_non_empty_floor, item_count, current_index
            )
            remaining_floors: tuple[int, Floor] = [
                (i, floor)
                for i, floor in enumerate(self.floors[:3])
                if i not in {self.lowest_non_empty_floor, current_index}
                and not floor.is_empty
            ]

        for i, floor in remaining_floors:
            output += self.cost_to_clear_floor(i, len(floor.things), 3)
        return output

    @staticmethod
    def cost_to_clear_floor(floor: int, item_count: int, from_floor: int):
        dist_to_top = 3 - floor
        one_way_trips = item_count * 2 - 1
        return dist_to_top * one_way_trips + abs(floor - from_floor)

    @cached_property
    def lowest_non_empty_floor(self) -> int:
        for i, floor in enumerate(self.floors):
            if not floor.is_empty:
                return i

        assert False

    @cached_property
    def is_victory(self) -> bool:
        return all([floor.is_empty for floor in self.floors[:3]])

    @cached_property
    def floor_count(self) -> int:
        return len(self.floors)

    @cached_property
    def current_floor(self) -> Floor:
        return self.floors[self.current_floor_index]

    @property
    def is_valid(self) -> bool:
        return all([floor.is_valid for floor in self.floors])

    @property
    def valid_elevator_directions(self) -> Iterator[int]:
        if self.current_floor_index > 0:
            yield -1
        if self.current_floor_index < 3:
            yield 1

    def move_things(self, things: set[Thing], direction: int) -> State:
        prev_floor_index = self.current_floor_index
        next_floor_index = self.current_floor_index + direction
        prev_floor = self.floors[prev_floor_index]
        next_floor = self.floors[next_floor_index]

        assert 0 <= next_floor_index < self.floor_count
        for thing in things:
            assert thing in prev_floor.things
        new_things_on_prev_floor = prev_floor.things - things
        new_things_on_next_floor = frozenset([*next_floor.things, *things])

        new_floors: List[Floor] = []
        for level, floor in enumerate(self.floors):
            if level == prev_floor_index:
                new_floors.append(Floor(things=new_things_on_prev_floor))
            elif level == next_floor_index:
                new_floors.append(Floor(things=new_things_on_next_floor))
            else:
                new_floors.append(floor)

        return State(
            floors=tuple(new_floors),
            current_floor_index=next_floor_index,
            steps=self.steps + 1,
        )

    @cached_property
    def core_state(self) -> CoreState:
        return CoreState(
            current_floor_index=self.current_floor_index,
            floors=tuple([floor.core_floor for floor in self.floors]),
            steps=self.steps,
        )
