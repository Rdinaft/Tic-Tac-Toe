import random
from typing import Optional
from preparing import Signs


def put_player_sign(player_sign: Signs, field: list[list[Optional[str]]]) -> None:
    print("---------Your turn!---------")
    not_over = True
    while not_over:
        move_line, move_column = input("Enter coordinates with space: ").split()
        move_line, move_column = int(move_line), int(move_column)
        if field[move_line][move_column] is None:
            field[move_line][move_column] = player_sign
            not_over = False


def put_computer_sign(computer_sign: Signs, field: list[list[Optional[str]]], num_of_lines: int) -> None:
    print("-------Computer turn!-------")
    not_over = True
    while not_over:
        line_coordinate = random.randint(0, num_of_lines - 1)
        column_coordinate = random.randint(0, num_of_lines - 1)
        if field[line_coordinate][column_coordinate] is None:
            field[line_coordinate][column_coordinate] = computer_sign
            not_over = False
