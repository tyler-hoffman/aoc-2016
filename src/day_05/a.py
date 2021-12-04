import hashlib

def solve(id: str) -> str:
    output = ""
    index = 0

    while len(output) < 8:
        to_hash = f"{id}{index}"
        hashed = hashlib.md5(to_hash.encode()).hexdigest()

        if hashed.startswith("00000"):
            output += hashed[5]
        index += 1


    return output


if __name__ == "__main__":
    input = "ugkcyxxp"
    print(solve(input))
