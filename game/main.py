from choosing_sides import (
    display_greetings,
    ask_player_side,
    assign_signs,
    output_player_side,
)
from field import draw_field, create_field
from game_state import (
    get_winner_per_row,
    get_winner_per_column,
    get_winner_per_diagonal,
    check_for_tie,
    spot_the_winner,
)
from game_progress import (
    take_coordinates_from_player,
    take_coordinates_from_computer,
    first_turn_move,
)
from constants import FIELD_SIZE
from enums import Sign


if __name__ == "__main__":
    field = create_field(FIELD_SIZE)
    display_greetings()
    chosen_side = ask_player_side()
    output_player_side(chosen_side)
    player_sign, computer_sign = assign_signs(chosen_side)
    sign_dict = {"Computer": computer_sign, "Player": player_sign}

    draw_field(field, Sign)
    first_turn_move(chosen_side, FIELD_SIZE, field, player_sign)

    while not any(
        [
            get_winner_per_row(sign_dict, field, FIELD_SIZE),
            get_winner_per_column(sign_dict, field, FIELD_SIZE),
            get_winner_per_diagonal(sign_dict, field, FIELD_SIZE),
            check_for_tie(field),
        ]
    ):
        take_coordinates_from_computer(computer_sign, field, FIELD_SIZE)
        draw_field(field, Sign)
        if any(
            [
                get_winner_per_row(sign_dict, field, FIELD_SIZE),
                get_winner_per_column(sign_dict, field, FIELD_SIZE),
                get_winner_per_diagonal(sign_dict, field, FIELD_SIZE),
                check_for_tie(field),
            ]
        ):
            continue
        take_coordinates_from_player(player_sign, field)
        draw_field(field, Sign)
    else:
        print(f"--------{spot_the_winner(sign_dict, field, FIELD_SIZE)} won!--------")
