import random
from choosing_sides import Signs


def first_turn_move(chosen_side: str, signs: Signs, num_of_lines: int, field: list[list[str | None]], player_sign: Signs) -> None:
    for line in range(num_of_lines):
        if field[line] == [None, None, None] and chosen_side == signs.crosses.name:
            return put_player_sign(player_sign, field)
        else:
            pass


def put_player_sign(player_sign: Signs, field: list[list[str | None]]) -> None:
    print("---------Your turn!---------")
    not_over = True
    while not_over:
        move_line, move_column = input("Enter coordinates with space: ").split()
        move_line, move_column = int(move_line), int(move_column)
        if field[move_line][move_column] is None:
            field[move_line][move_column] = player_sign
            not_over = False


def put_computer_sign(computer_sign: Signs, field: list[list[str | None]], num_of_lines: int) -> None:
    print("-------Computer turn!-------")
    not_over = True
    while not_over:
        line_coordinate = random.randint(0, num_of_lines - 1)
        column_coordinate = random.randint(0, num_of_lines - 1)
        if field[line_coordinate][column_coordinate] is None:
            field[line_coordinate][column_coordinate] = computer_sign
            not_over = False
