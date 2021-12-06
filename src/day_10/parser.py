import re
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, List

from src.day_10.models import Bot, Output


@dataclass
class Data(object):
    bots: List[Bot]
    outputs: List[Output]


class Parser(object):
    @cached_property
    def value_goes_to_bot_pattern(self):
        return re.compile(r"value (\d+) goes to bot (\d+)")

    @cached_property
    def bot_gives_value_pattern(self):
        return re.compile(r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)")

    def parse(self, input: str) -> Data:
        bots = self.create_bots(input)
        outputs = self.create_outputs(input)

        for line in input.strip().splitlines():
            self.parse_instruction(line, bots, outputs)

        return Data(bots=list(bots.values()), outputs=list(outputs.values()))

    def parse_instruction(
        self, line: str, bots: Dict[int, Bot], outputs: Dict[int, Output]
    ) -> None:
        if (match := self.value_goes_to_bot_pattern.search(line)) is not None:
            value = int(match.group(1))
            bot = bots[int(match.group(2))]
            bot.start_values.append(value)
        elif (match := self.bot_gives_value_pattern.search(line)) is not None:
            bot_id = int(match.group(1))
            low_entity_type = match.group(2)
            low_entity_id = int(match.group(3))
            high_entity_type = match.group(4)
            high_entity_id = int(match.group(5))

            giver = bots[bot_id]
            low_entity = (
                bots[low_entity_id]
                if low_entity_type == "bot"
                else outputs[low_entity_id]
            )
            high_entity = (
                bots[high_entity_id]
                if high_entity_type == "bot"
                else outputs[high_entity_id]
            )

            giver.give_low = low_entity
            giver.give_high = high_entity
        else:
            raise Exception(f'Unable to parse line "{line}"')

    def create_bots(self, input: str) -> Dict[int, Bot]:
        output: Dict[int, Bot] = {}
        for match in re.findall(r"bot \d+", input):
            _, value = match.split(" ")
            id = int(value)
            output[id] = Bot(id=id)
        return output

    def create_outputs(self, input: str) -> Dict[int, Output]:
        output: Dict[int, Output] = {}
        for match in re.findall(r"bot \d+", input):
            _, value = match.split(" ")
            id = int(value)
            output[id] = Output(id=id)
        return output
