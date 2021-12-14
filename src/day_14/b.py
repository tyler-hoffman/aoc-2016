from src.day_14.solver import Solver


def solve(salt: str) -> int:
    solver = Solver(salt=salt.strip(), hashes_per_string=2017)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_14/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
