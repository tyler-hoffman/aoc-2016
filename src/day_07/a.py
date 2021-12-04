from src.day_07.shared import parse


def solve(input: str) -> int:
    ip_addresses = parse(input)

    return len([address for address in ip_addresses if address.supports_tls])


if __name__ == "__main__":
    with open("src/day_07/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
