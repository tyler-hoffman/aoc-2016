import os

from utils.boilerplate.file_data import FileData
from utils.boilerplate.parser import create_parser
from utils.boilerplate.templates.part import PART_TEMPLATE
from utils.boilerplate.templates.test_part import TEST_PART_TEMPLATE


def create_directories_if_needed(file_data: FileData) -> None:
    if not os.path.isdir(file_data.directory):
        os.makedirs(file_data.directory)
        open(file_data.src_init_file, "x")
        open(file_data.input_file, "x")

    if not os.path.isdir(file_data.test_directory):
        os.makedirs(file_data.test_directory)
        open(file_data.test_init_file, "x")


def create_part_files(file_data: FileData) -> None:
    with open(file_data.part_file, "w") as f:
        content = PART_TEMPLATE.format(
            day_string=file_data.day_string, part=file_data.part
        )
        f.write(content.strip() + "\n")

    with open(file_data.test_part_file, "w") as f:
        content = TEST_PART_TEMPLATE.format(
            day_string=file_data.day_string,
            part=file_data.part,
            part_upper=file_data.part.upper(),
        )
        f.write(content.strip() + "\n")


if __name__ == "__main__":
    args = create_parser().parse_args()

    file_data = FileData(day=args.day, part=args.part)

    create_directories_if_needed(file_data)
    create_part_files(file_data)
