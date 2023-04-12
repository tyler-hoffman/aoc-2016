from dataclasses import dataclass, field
from functools import cached_property


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
    discriminator: str | int
    offset: str | int


@dataclass
class Tgl(object):
    offset: str | int


Instruction = Inc | Dec | Cpy | Jnz | Tgl


@dataclass
class Machine(object):
    instructions: list[Instruction]
    registers: dict[str, int] = field(
        default_factory=lambda: {r: 0 for r in ("a", "b", "c", "d")}
    )
    pointer: int = 0

    def run(self):
        while 0 <= self.pointer < len(self.instructions):
            if self.toggled_registers[self.pointer]:
                self.run_toggled()
            else:
                self.run_non_toggled()
            self.pointer += 1

    def run_toggled(self):
        match self.current_instruction:
            case Inc(register):
                self.registers[register] -= 1
            case Dec(register):
                self.registers[register] += 1
            case Cpy(value, offset):
                if self.value(value):
                    self.pointer += self.value(offset) - 1
            case Jnz(value, register):
                if isinstance(register, str):
                    self.registers[register] = self.value(value)
            case Tgl(register):
                if isinstance(register, str):
                    self.registers[register] += 1

    def run_non_toggled(self):
        match self.current_instruction:
            case Inc(register):
                self.registers[register] += 1
            case Dec(register):
                self.registers[register] -= 1
            case Cpy(value, register):
                self.registers[register] = self.value(value)
            case Jnz(value, offset):
                if self.value(value):
                    self.pointer += self.value(offset) - 1
            case Tgl(offset):
                index = self.pointer + self.value(offset)
                if 0 <= index < len(self.instructions):
                    self.toggled_registers[index] = not self.toggled_registers[index]

    @cached_property
    def toggled_registers(self) -> list[bool]:
        return [False for _ in self.instructions]

    @property
    def current_instruction(self) -> Instruction:
        return self.instructions[self.pointer]

    def value(self, value: str | int) -> int:
        if isinstance(value, int):
            return value
        else:
            return self.registers[value]
