from typing import Optional
from preparing import Signs


def is_game_ended(
    computer_sign: Signs, player_sign: Signs, field: list[list[Optional[str]]], num_of_lines: int
) -> str | bool:
    sign_dict = {"Computer": computer_sign, "Player": player_sign}
    for participant in sign_dict:
        for line in range(num_of_lines):
            if field[line] == [sign_dict[participant]] * len(field[line]):
                return participant
            elif list(map(list, zip(*field)))[line] == [sign_dict[participant]] * len(field[line]):
                return participant
            '''elif field[0][0] == field[line][line] == field[-1][-1] == sign_dict[participant]:
                return participant
            elif field[0][-1] == field[line][line] == field[-1][0] == sign_dict[participant]:
                return participant'''
    return False


def is_it_tie():
    return False
