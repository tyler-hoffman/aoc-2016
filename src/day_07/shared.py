import dataclasses
import re
from typing import List

@dataclasses.dataclass
class IpAddress(object):
    value: str

    @property
    def supports_tls(self) -> bool:
        return self._parts_contain_abba(self._outer_parts) and not self._parts_contain_abba(self._inner_parts)

    def _parts_contain_abba(self, parts: List[str]) -> bool:
        return any([self._part_contains_abba(part) for part in parts])

    def _part_contains_abba(self, part: str) -> bool:
        part_len = len(part)
        for i in range(part_len - 3):
            a, b, c, d = list(part[i:i+4])
            if all([a==d, b==c, a != b ]):
                return True
        return False


    @property
    def _outer_parts(self) -> List[str]:
        parts = re.split("\]|\[", self.value)

        return [part for i, part in enumerate(parts) if i % 2 == 0]

    @property
    def _inner_parts(self) -> List[str]:
        parts = re.split("\]|\[", self.value)

        return [part for i, part in enumerate(parts) if i % 2 == 1]

def parse(input: str) -> List[IpAddress]:
    return [IpAddress(x) for x in input.strip().splitlines()]
