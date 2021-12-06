from dataclasses import dataclass
from typing import List, Set, Tuple
from src.day_10.instructions import Bot, Instruction, Output
from src.day_10.parser import Parser
from src.day_10.solver import Solver

@dataclass
class Day10PartBSolver(Solver):
    bots: List[Bot]
    outputs: List[Output]
    instructions: List[Instruction]
    target_values: Set[int]

    @property
    def solution(self) -> int:
        self.setup()

        while len([bot for bot in self.bots if bot.ready_to_give]):
            bots_ready_to_give = [bot for bot in self.bots if bot.ready_to_give]
            assert len(bots_ready_to_give) > 0
            for bot in bots_ready_to_give:
                bot.give_low.values.append(min(bot.values))
                bot.give_high.values.append(max(bot.values))
                bot.values = []

        output = 1
        outputs_in_question = [x for x in self.outputs if x.id in {0, 1, 2}]
        for x in outputs_in_question:
            output *= x.values[-1]
        return output


    def setup(self) -> None:
        for bot in self.bots:
            bot.values = bot.start_values.copy()


def solve(input: str, values: Tuple[int, int]) -> int:
    parser = Parser()
    data = parser.parse(input)
    solver = Day10PartBSolver(**data.__dict__, target_values=set(values))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_10/input.txt", "r") as f:
        input = f.read()
    print(solve(input, (61, 17)))
