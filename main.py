from constants import SIGN_LIST
from preparing import display_greetings, choose_side, assign_signs, is_player_first_turn
from field import draw_field, calculate_field_size
from game_state import is_game_ended
from gameplay import put_computer_sign, put_player_sign


if __name__ == "__main__":
    field_list = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    chosen = display_greetings(SIGN_LIST)
    chosen_side = choose_side(chosen, SIGN_LIST)
    player_sign, computer_sign = assign_signs(chosen_side, SIGN_LIST)
    first_turn = is_player_first_turn(chosen_side)
    draw_field(field_list)

    while is_game_ended(computer_sign, player_sign, field_list, calculate_field_size(field_list)) == False:
        if first_turn:
            put_player_sign(player_sign, field_list)
            draw_field(field_list)
            put_computer_sign(computer_sign, field_list, calculate_field_size(field_list))
            draw_field(field_list)
        else:
            put_computer_sign(computer_sign, field_list, calculate_field_size(field_list))
            draw_field(field_list)
            put_player_sign(player_sign, field_list)
            draw_field(field_list)
    else:
        print(
            f"---------{is_game_ended(computer_sign, player_sign, field_list, calculate_field_size(field_list))} wins!---------"
        )
