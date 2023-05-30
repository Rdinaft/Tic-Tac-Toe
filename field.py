from typing import Optional


def calculate_field_size(field: list[list[Optional[str]]]) -> int:
    num_of_lines = 0
    for line in field:
        if type(line) == list:
            num_of_lines += 1
    return num_of_lines


def draw_field(field: list[list[Optional[str]]]) -> None:
    for line in field:
        print(line)
