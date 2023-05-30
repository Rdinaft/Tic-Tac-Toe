import random
import enum


def display_greetings(signs: list[str]) -> str:
    print("Welcome to Tic-Tac-Toe!")
    chosen = input("Choose your side (random, naughts, crosses): ").lower()
    while chosen not in signs + ["random"]:
        chosen = input("Try again: ").lower()
    return chosen


def choose_side(chosen: str, signs: list[str]) -> str:
    if chosen == "random":
        chosen_side = random.choice(signs)
    else:
        chosen_side = chosen
    print(f"Okay, you choose {chosen_side}!")
    return chosen_side


class Signs(enum.Enum):
    X = 'X'
    O = 'O'


def assign_signs(chosen_side: str, signs: list[str]) -> tuple[str, str]:
    if chosen_side == signs[0]:
        player_sign = Signs.O.value
        computer_sign = Signs.X.value
    else:
        player_sign = Signs.X.value
        computer_sign = Signs.O.value
    return player_sign, computer_sign


def is_player_first_turn(chosen_side: str) -> bool:
    if chosen_side == "crosses":
        return True
    else:
        return False
