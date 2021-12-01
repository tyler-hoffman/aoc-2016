from typing import Dict, List, TypeVar


T = TypeVar("T")


def frequency_map(items: List[T]) -> Dict[T, int]:
    output: Dict[T, int] = dict()

    for item in items:
        output[item] = output.get(item, 0) + 1

    return output
