import hashlib
from typing import Iterator


def get_hashes_for_prefix(prefix: str) -> Iterator[str]:
    index = 0

    while True:
        to_hash = f"{prefix}{index}"
        hashed = hashlib.md5(to_hash.encode()).hexdigest()
        if hashed.startswith("00000"):
            yield hashed
        index += 1
