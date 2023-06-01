from enums import Signs


def display_greetings() -> None:
    print("Welcome to Tic-Tac-Toe!")


def ask_player_side() -> str:
    chosen_side = input("Choose your side (naughts, crosses): ").lower()
    while chosen_side not in [signs.name for signs in Signs]:
        chosen_side = input("Try again: ").lower()
    return chosen_side


def output_player_side(chosen_side: str) -> None:
    print(f"Okay, you choose {chosen_side}!")


def assign_signs(chosen_side: str, signs: Signs) -> tuple[Signs, Signs]:
    if chosen_side == signs.naughts.name:
        player_sign = signs.naughts.value
        computer_sign = signs.crosses.value
    else:
        player_sign = signs.crosses.value
        computer_sign = signs.naughts.value
    return player_sign, computer_sign
