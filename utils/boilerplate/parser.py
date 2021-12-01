import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Helper to bootstrap files for problems"
    )
    parser.add_argument("-d", "--day", type=int, help="Day to create files for")
    parser.add_argument(
        "-p",
        "--part",
        choices=["a", "b"],
        help="Part to create files for",
    )

    return parser
