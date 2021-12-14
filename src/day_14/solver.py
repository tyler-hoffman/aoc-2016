from dataclasses import dataclass, field
from hashlib import md5
from more_itertools import nth, sliding_window
from queue import Queue
from typing import Iterator, Optional


@dataclass
class Key(object):
    value: str
    triple: str
    index: int
    found_match: bool = False

    def __hash__(self):
        return hash((self.value, self.triple, self.index))


@dataclass
class Solver(object):
    salt: str
    hashes_per_string: int
    triple_to_keys: dict[str, set[Key]] = field(default_factory=dict)
    key_queue: Queue[Optional[Key]] = field(default_factory=Queue)

    @property
    def solution(self) -> int:
        return nth(self.get_keys(), 63).index

    def get_keys(self) -> Iterator[Key]:
        index = 0

        while True:
            if index > 1000:
                if key := self.key_queue.get():
                    self.triple_to_keys[key.triple].remove(key)
                    if key.found_match:
                        yield key

            hashed = self.hash_it_up(f"{self.salt}{index}")
            triple = self.get_first_run(hashed, 3)
            pentuple = self.get_first_run(hashed, 5)

            if pentuple:
                if keys := self.triple_to_keys.get(triple):
                    for k in keys:
                        k.found_match = True

            if triple:
                key = Key(value=hashed, triple=triple, index=index)
                self.key_queue.put(key)
                if not self.triple_to_keys.get(triple):
                    self.triple_to_keys[triple] = set()
                self.triple_to_keys[triple].add(key)
            else:
                self.key_queue.put(None)
            index += 1

    def hash_it_up(self, string: str) -> str:
        string = md5(string.encode()).hexdigest()

        for _ in range(self.hashes_per_string - 1):
            string = md5(string.encode()).hexdigest()
        return string

    @staticmethod
    def get_first_run(string: str, count: int) -> Optional[str]:
        for window in sliding_window(string, count):
            if len(set(window)) == 1:
                return window[0] * count
        return None
