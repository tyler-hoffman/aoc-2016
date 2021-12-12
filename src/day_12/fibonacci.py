from typing import Iterator


def fibonacci_sequence() -> Iterator[int]:
    prev = 0
    curr = 1

    while True:
        yield curr
        prev, curr = curr, prev + curr
