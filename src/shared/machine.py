from dataclasses import dataclass, field


@dataclass
class Inc(object):
    register: str


@dataclass
class Dec(object):
    register: str


@dataclass
class Cpy(object):
    value: str | int
    register: str


@dataclass
class Jnz(object):
    register: str | int
    offset: int


Instruction = Inc | Dec | Cpy | Jnz


@dataclass
class Machine(object):
    instructions: list[Instruction]
    registers: dict[str, int] = field(
        default_factory=lambda: {r: 0 for r in ("a", "b", "c", "d")}
    )
    pointer: int = 0

    def run(self):
        while 0 <= self.pointer < len(self.instructions):
            match self.current_instruction:
                case Inc(register):
                    self.registers[register] += 1
                case Dec(register):
                    self.registers[register] -= 1
                case Cpy(value, register):
                    self.registers[register] = self.value(value)
                case Jnz(value, offset):
                    if self.value(value):
                        self.pointer += offset - 1
            self.pointer += 1

    @property
    def current_instruction(self) -> Instruction:
        return self.instructions[self.pointer]

    def value(self, value: str | int) -> int:
        if isinstance(value, int):
            return value
        else:
            return self.registers[value]
