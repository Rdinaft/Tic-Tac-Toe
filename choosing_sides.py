from enums import Sign


def display_greetings() -> None:
    print("Welcome to Tic-Tac-Toe!")


def ask_player_side() -> str:
    chosen_side = input("Choose your side (naughts, crosses): ").lower()
    while chosen_side not in [signs.name for signs in Sign]:
        chosen_side = input("Try again: ").lower()
    return chosen_side


def output_player_side(chosen_side: str) -> None:
    print(f"Okay, you choose {chosen_side}!")


def assign_signs(chosen_side: str) -> tuple[str, str]:
    name = Sign.naughts.name
    naughts_sign = Sign.naughts.value
    crosses_sign = Sign.crosses.value
    if chosen_side == name:
        player_sign = naughts_sign
        computer_sign = crosses_sign
    else:
        player_sign = crosses_sign
        computer_sign = naughts_sign
    return player_sign, computer_sign
