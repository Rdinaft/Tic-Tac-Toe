import random
from choosing_sides import Signs


def first_turn_move(
    chosen_side: str,
    signs: Signs,
    num_of_lines: int,
    field: list[list[Signs | None]],
    player_sign: Signs,
) -> None:
    for line in range(num_of_lines):
        if field[line] == [None] * num_of_lines and chosen_side == signs.crosses.name:
            return ask_player_for_coordinates(player_sign, field)


def ask_player_for_coordinates(
    player_sign: Signs, field: list[list[Signs | None]], sign_not_placed: bool = True
) -> None:
    print("---------Your turn!---------")
    while sign_not_placed:
        try:
            line_coordinate, column_coordinate = input(
                "Enter coordinates with space: "
            ).split()
            line_coordinate, column_coordinate = int(line_coordinate), int(
                column_coordinate
            )
            if (
                check_for_sign_in_coordinate(field, line_coordinate, column_coordinate)
                is False
            ):
                put_sign_on_field(
                    player_sign, field, line_coordinate, column_coordinate
                )
        except (ValueError, IndexError):
            print("Try again!")
            continue
        sign_not_placed = False


def ask_computer_for_coordinates(
    computer_sign: Signs,
    field: list[list[Signs | None]],
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
    sign: Signs,
    field: list[list[Signs | None]],
    line_coordinate: int,
    column_coordinate: int,
) -> None:
    while field[line_coordinate][column_coordinate] is None:
        field[line_coordinate][column_coordinate] = sign


def check_for_sign_in_coordinate(
    field: list[list[Signs | None]], line_coordinate: int, column_coordinate: int
) -> bool:
    if field[line_coordinate][column_coordinate] is None:
        return False
    return True
