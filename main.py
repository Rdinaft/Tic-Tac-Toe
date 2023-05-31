from choosing_sides import display_greetings, player_enter_side, assign_signs, output_player_side
from field import draw_field, calculate_field_size
from game_state import get_winner_per_row, get_winner_per_column, get_winner_per_diagonal, check_for_tie, spot_the_winner
from game_progress import put_computer_sign, put_player_sign, first_turn_move
from enums import Signs


if __name__ == "__main__":
    field_list = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    display_greetings()
    chosen_side = player_enter_side()
    output_player_side(chosen_side)
    player_sign, computer_sign = assign_signs(chosen_side, Signs)
    sign_dict = {"Computer": computer_sign, "Player": player_sign}
    num_of_lines = calculate_field_size(field_list)

    draw_field(field_list)
    first_turn_move(chosen_side, Signs, num_of_lines, field_list, player_sign)
    
    while not any([get_winner_per_row(sign_dict, field_list, num_of_lines), get_winner_per_column(sign_dict, field_list, num_of_lines), get_winner_per_diagonal(sign_dict, field_list, num_of_lines), check_for_tie(field_list)]):
        draw_field(field_list)
        put_computer_sign(computer_sign, field_list, num_of_lines)
        if any([get_winner_per_row(sign_dict, field_list, num_of_lines), get_winner_per_column(sign_dict, field_list, num_of_lines), get_winner_per_diagonal(sign_dict, field_list, num_of_lines), check_for_tie(field_list)]):
            continue
        draw_field(field_list)
        put_player_sign(player_sign, field_list)
    else:
        draw_field(field_list)
        print(f"--------{spot_the_winner(sign_dict, field_list, num_of_lines)} won!--------")
