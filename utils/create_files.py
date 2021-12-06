import argparse
import aocd
import os

from utils.file_data import FileData
from utils.templates.part import PART_TEMPLATE
from utils.templates.parser import PARSER_TEMPLATE
from utils.templates.solver import SOLVER_TEMPLATE
from utils.templates.test_part import TEST_PART_TEMPLATE
from utils.templates.test_data import TEST_DATA_TEMPLATE


def touch_file(path: str) -> None:
    open(path, "x")


def write_file(path: str, content: str) -> None:
    with open(path, "w") as f:
        f.write(content.strip() + "\n")


def create_directories_if_needed(file_data: FileData) -> None:
    if not os.path.isdir(file_data.directory):
        os.makedirs(file_data.directory)
        touch_file(file_data.src_init_file)
        write_file(file_data.input_file, aocd.get_data(year=2016, day=file_data.day))
        write_file(
            file_data.parser_file,
            PARSER_TEMPLATE.format(day_string=file_data.day_string),
        )
        write_file(
            file_data.solver_file,
            SOLVER_TEMPLATE.format(day_string=file_data.day_string),
        )

    if not os.path.isdir(file_data.test_directory):
        os.makedirs(file_data.test_directory)
        touch_file(file_data.test_init_file)
        write_file(file_data.test_data_file, TEST_DATA_TEMPLATE)


def create_part_files(file_data: FileData) -> None:
    write_file(
        file_data.part_file,
        PART_TEMPLATE.format(day_string=file_data.day_string, part=file_data.part),
    )

    write_file(
        file_data.test_part_file,
        TEST_PART_TEMPLATE.format(
            day_string=file_data.day_string,
            part=file_data.part,
            part_upper=file_data.part.upper(),
        ),
    )


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


if __name__ == "__main__":
    args = create_parser().parse_args()

    file_data = FileData(day=args.day, part=args.part)

    create_directories_if_needed(file_data)
    create_part_files(file_data)
