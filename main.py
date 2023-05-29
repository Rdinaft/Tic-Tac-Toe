import random
from typing import Optional
from constants import SIGN_LIST, FIELD_FROM, FIELD_TO, COLUMNS, FIELD_LIST


def greetings(signs: list[str]) -> str:
    print("Welcome to Tic-Tac-Toe!")
    chosen = input("Choose your side (random, naughts, crosses): ").lower()
    while chosen not in signs + ["random"]:
        chosen = input("Choose your side (random, naughts, crosses): ").lower()
    return chosen


def choose_side(chosen: str, signs: list[str]) -> str:
    if chosen == "random":
        chosen_side = random.choice(signs)
    else:
        chosen_side = chosen
    print(f"Okay, you choose {chosen_side}!")
    return chosen_side


def signs_definition(chosen_side: str, signs: list[str]) -> tuple[str, str]:
    if chosen_side == signs[0]:
        player_sign = "O"
        computer_sign = "X"
    else:
        player_sign = "X"
        computer_sign = "O"
    return player_sign, computer_sign


def is_player_first_turn(chosen_side: str) -> bool:
    if chosen_side == "crosses":
        return True
    else:
        return False


def player_turn(player_sign: str, field: list[list[Optional[str]]]) -> None:
    print("---------Your turn!---------")
    not_over = True
    while not_over:
        coordinates = input("Enter coordinates with space: ").split()
        move_line, move_column = coordinates
        move_line = int(move_line)
        move_column = int(move_column)
        if field[move_line][move_column] is None:
            field[move_line][move_column] = player_sign
            not_over = False
    draw_field(FIELD_LIST)


def computer_turn(computer_sign: str, field: list[list[Optional[str]]]) -> None:
    print("-------Computer turn!-------")
    not_over = True
    while not_over:
        line_coordinate = random.randint(FIELD_FROM, FIELD_TO)
        column_coordinate = random.randint(FIELD_FROM, FIELD_TO)
        if field[line_coordinate][column_coordinate] is None:
            field[line_coordinate][column_coordinate] = computer_sign
            not_over = False
    draw_field(FIELD_LIST)


def is_game_ended(
    computer_sign: str, player_sign: str, field: list[list[Optional[str]]]
) -> str | bool:
    sign_dict = {"Computer": computer_sign, "Player": player_sign}
    for participant in sign_dict:
        if field[0] == [sign_dict[participant]] * COLUMNS:
            return participant
        elif field[1] == [sign_dict[participant]] * COLUMNS:
            return participant
        elif field[2] == [sign_dict[participant]] * COLUMNS:
            return participant
        elif (
            field[0][0] == sign_dict[participant]
            and field[1][0] == sign_dict[participant]
            and field[2][0] == sign_dict[participant]
        ):
            return participant
        elif (
            field[0][1] == sign_dict[participant]
            and field[1][1] == sign_dict[participant]
            and field[2][1] == sign_dict[participant]
        ):
            return participant
        elif (
            field[0][2] == sign_dict[participant]
            and field[1][2] == sign_dict[participant]
            and field[2][2] == sign_dict[participant]
        ):
            return participant
        elif (
            field[0][0] == sign_dict[participant]
            and field[1][1] == sign_dict[participant]
            and field[2][2] == sign_dict[participant]
        ):
            return participant
        elif (
            field[0][2] == sign_dict[participant]
            and field[1][1] == sign_dict[participant]
            and field[2][0] == sign_dict[participant]
        ):
            return participant
    return False


def draw_field(field: list[list[Optional[str]]]) -> None:
    for line in field:
        print(line)


if __name__ == "__main__":
    chosen = greetings(SIGN_LIST)
    chosen_side = choose_side(chosen, SIGN_LIST)
    player_sign, computer_sign = signs_definition(chosen_side, SIGN_LIST)
    first_turn = is_player_first_turn(chosen_side)
    draw_field(FIELD_LIST)

    while is_game_ended(computer_sign, player_sign, FIELD_LIST) == False:
        if first_turn:
            player_turn(player_sign, FIELD_LIST)
            computer_turn(computer_sign, FIELD_LIST)
        else:
            computer_turn(computer_sign, FIELD_LIST)
            player_turn(player_sign, FIELD_LIST)
    else:
        print(
            f"---------{is_game_ended(computer_sign, player_sign, FIELD_LIST)} wins!---------"
        )

# сделать каким-то образом ничью                         ???
# закончить цикл is game ended сразу после смены на тру  ???
# по-другому сделать первый ход                          ???
