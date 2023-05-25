import random
import sys
from constants import SIGN_LIST, FIELD_FROM, FIELD_TO, COLUMNS, FIELD_LIST


def greetings() -> str:
    print("Welcome to Tic-Tac-Toe!")
    chosen = input("Choose your side (random, naughts, crosses): ").lower()
    while chosen not in SIGN_LIST + ["random"]:
        chosen = input("Choose your side (random, naughts, crosses): ").lower()
    return chosen


def choose_side(chosen: str) -> str:
    if chosen == "random":
        chosen_side = random.choice(SIGN_LIST)
    else:
        chosen_side = chosen
    print(f"Okay, you choose {chosen_side}!")
    return chosen_side


def signs_definition(chosen_side: str) -> tuple[str, str]:
    if chosen_side == SIGN_LIST[0]:
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


def player_turn(player_sign: str) -> None:
    print("---------Your turn!---------")
    not_over = True
    while not_over:
        move = input("Enter coordinate: ")
        for line in FIELD_LIST:
            if move in line:
                index = line.index(move)
                line[index] = player_sign
                not_over = False
    draw_field(FIELD_LIST)


def computer_turn(computer_sign: str) -> None:
    print("-------Computer turn!-------")
    not_over = True
    while not_over:
        coordinate = str(random.randint(FIELD_FROM, FIELD_TO))
        for line in FIELD_LIST:
            if coordinate in line:
                index = line.index(coordinate)
                line[index] = computer_sign
                not_over = False
    draw_field(FIELD_LIST)


def is_game_ended(computer_sign: str, player_sign: str) -> None:
    sign_dict = {"Computer": computer_sign, "Player": player_sign}
    for participant in sign_dict:
        if FIELD_LIST[0] == [sign_dict[participant]] * COLUMNS:
            print(f"---------{participant} wins!---------")
            return True
        elif FIELD_LIST[1] == [sign_dict[participant]] * COLUMNS:
            print(f"---------{participant} wins!---------")
            return True
        elif FIELD_LIST[2] == [sign_dict[participant]] * COLUMNS:
            print(f"---------{participant} wins!---------")
            return True
        elif (
            FIELD_LIST[0][0] == sign_dict[participant]
            and FIELD_LIST[1][0] == sign_dict[participant]
            and FIELD_LIST[2][0] == sign_dict[participant]
        ):
            print(f"---------{participant} wins!---------")
            return True
        elif (
            FIELD_LIST[0][1] == sign_dict[participant]
            and FIELD_LIST[1][1] == sign_dict[participant]
            and FIELD_LIST[2][1] == sign_dict[participant]
        ):
            print(f"---------{participant} wins!---------")
            return True
        elif (
            FIELD_LIST[0][2] == sign_dict[participant]
            and FIELD_LIST[1][2] == sign_dict[participant]
            and FIELD_LIST[2][2] == sign_dict[participant]
        ):
            print(f"---------{participant} wins!---------")
            return True
        elif (
            FIELD_LIST[0][0] == sign_dict[participant]
            and FIELD_LIST[1][1] == sign_dict[participant]
            and FIELD_LIST[2][2] == sign_dict[participant]
        ):
            print(f"---------{participant} wins!---------")
            return True
        elif (
            FIELD_LIST[0][2] == sign_dict[participant]
            and FIELD_LIST[1][1] == sign_dict[participant]
            and FIELD_LIST[2][0] == sign_dict[participant]
        ):
            print(f"---------{participant} wins!---------")
            return True
    return False


def is_it_tie() -> bool:
    return False


def draw_field(field: list[list[str]]) -> None:
    return print(*field, sep="\n")


if __name__ == "__main__":
    chosen = greetings()
    chosen_side = choose_side(chosen)
    player_sign, computer_sign = signs_definition(chosen_side)
    first_turn = is_player_first_turn(chosen_side)
    draw_field(FIELD_LIST)

    while is_game_ended(computer_sign, player_sign) == False:
        if first_turn:
            player_turn(player_sign)
            computer_turn(computer_sign)
        else:
            computer_turn(computer_sign)
            player_turn(player_sign)
    else:
        sys.exit(0)
