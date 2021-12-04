from typing import List


def parse(input: str) -> List[str]:
    return [line for line in input.splitlines() if line]
