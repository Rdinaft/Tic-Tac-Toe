def calculate_field_size(field: list[list[str | None]]) -> int:
    num_of_lines = 0
    for line in field:
        num_of_lines += 1
    return num_of_lines


def draw_field(field: list[list[str | None]]) -> None:
    for line in field:
        print(line)
