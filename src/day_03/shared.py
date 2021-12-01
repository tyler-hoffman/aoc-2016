import dataclasses


@dataclasses.dataclass
class Triangle(object):
    a: int
    b: int
    c: int

    @property
    def is_valid(self) -> bool:
        half_length = sum([self.a, self.b, self.c]) / 2

        return all([x < half_length for x in [self.a, self.b, self.c]])
