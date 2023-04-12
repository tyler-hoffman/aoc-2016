from src.shared.machine import Cpy, Dec, Inc, Instruction, Jnz


class Parser(object):
    @classmethod
    def parse(cls, input: str) -> list[Instruction]:
        return [cls.parse_instruction(line) for line in input.strip().splitlines()]

    @classmethod
    def parse_instruction(cls, line: str) -> Instruction:
        words = line.split(" ")
        match words[0]:
            case "inc":
                return Inc(register=words[1])
            case "dec":
                return Dec(register=words[1])
            case "cpy":
                return Cpy(value=cls.parse_value(words[1]), register=words[2])
            case "jnz":
                return Jnz(discriminator=cls.parse_value(words[1]), offset=int(words[2]))
            case _:
                assert False

    @classmethod
    def parse_value(cls, word: str) -> int | str:
        if word.isnumeric():
            return int(word)
        else:
            return word
