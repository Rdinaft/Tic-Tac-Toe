import random
from choosing_sides import Sign


def first_turn_move(
    chosen_side: str,
    num_of_lines: int,
    field: list[list[str | None]],
    player_sign: str,
) -> None:
    crosses = Sign.crosses.name
    for line in range(num_of_lines):
        if field[line] == [None] * num_of_lines and chosen_side == crosses:
            return take_coordinates_from_player(player_sign, field)


def take_coordinates_from_player(
    player_sign: str, field: list[list[str | None]], sign_not_placed: bool = True
) -> None:
    print("---------Your turn!---------")
    while sign_not_placed:
        try:
            line_coordinate_str, column_coordinate_str = input(
                "Enter coordinates with space: "
            ).split()
            line_coordinate, column_coordinate = (
                int(line_coordinate_str),
                int(column_coordinate_str),
            )
            if not check_for_sign_in_coordinate(
                field, line_coordinate, column_coordinate
            ):
                put_sign_on_field(
                    player_sign, field, line_coordinate, column_coordinate
                )
                sign_not_placed = False
        except (ValueError, IndexError):
            print("Try again!")
            continue


def take_coordinates_from_computer(
    computer_sign: str,
    field: list[list[str | None]],
    num_of_lines: int,
    sign_not_placed: bool = True,
) -> None:
    print("-------Computer turn!-------")
    while sign_not_placed:
        line_coordinate = random.randint(0, num_of_lines - 1)
        column_coordinate = random.randint(0, num_of_lines - 1)
        if (
            check_for_sign_in_coordinate(field, line_coordinate, column_coordinate)
            is False
        ):
            put_sign_on_field(computer_sign, field, line_coordinate, column_coordinate)
            sign_not_placed = False


def put_sign_on_field(
    sign: str,
    field: list[list[str | None]],
    line_coordinate: int,
    column_coordinate: int,
) -> None:
    while field[line_coordinate][column_coordinate] is None:
        field[line_coordinate][column_coordinate] = sign


def check_for_sign_in_coordinate(
    field: list[list[str | None]], line_coordinate: int, column_coordinate: int
) -> bool:
    return field[line_coordinate][column_coordinate] is not None
