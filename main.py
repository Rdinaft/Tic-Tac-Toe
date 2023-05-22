import random


class Game:
    field_coordinates = {'top_left': ' ', 'top_middle': ' ', 'top_right': ' ', 'center_left': ' ', 'center_middle': ' ', 'center_right': ' ', 'bottom_left': ' ', 'bottom_middle': ' ', 'bottom_right': ' '}
    sign_list = ['naughts', 'crosses']
    end = False
    field = [
            [field_coordinates['top_left'], '|', field_coordinates['top_middle'], '|', field_coordinates['top_right']],
            ['---------------------'],
            [field_coordinates['center_left'], '|', field_coordinates['center_middle'], '|', field_coordinates['center_right']],
            ['---------------------'],
            [field_coordinates['bottom_left'], '|', field_coordinates['bottom_middle'], '|', field_coordinates['bottom_right']],
            ]

    def greetings(self) -> str:
        print('Welcome to Tic-Tac-Toe!')
        chosen = input('Choose your side (random, naughts, crosses): ').lower()
        return chosen

    def choose_side(self, chosen: str) -> str:
        if chosen == 'random':
            chosen_side = random.choice(self.sign_list)
        else:
            chosen_side = chosen
        self.sign_list.remove(chosen_side)
        print(f'Okay, you choose {chosen_side}!')
        return chosen_side

    def signs_definition(self, chosen_side: str) -> tuple[str, str]:
        if chosen_side == self.sign_list[0]:
            player_sign = 'O'
            computer_sign = 'X'
        else:
            player_sign = 'X'
            computer_sign = 'O'
        return player_sign, computer_sign

    def first_turn(self, chosen_side: str) -> bool | None:
        if chosen_side == 'crosses':
            print('Your turn!')
            return True
        else:
            return print('Computer turn!')

    def player_turn(self, player_sign: str) -> None:
        move = input('Enter coordinate: ').lower()
        if move in self.field_coordinates.keys() and self.field_coordinates[move] == ' ':
            self.field_coordinates[move] = player_sign

    def computer_turn(self, computer_sign: str) -> None:
        turn_not_over = True
        while turn_not_over:
            coordinate, placed_sign = random.choice(list(self.field_coordinates.items()))
            print(coordinate, placed_sign)
            if placed_sign == ' ' in self.field_coordinates:
                self.field_coordinates[coordinate] = computer_sign
            turn_not_over = False

    def end_game(self) -> None:
        if ' ' not in self.field_coordinates.values():
            self.end = True

    def draw_field(self) -> None:
        return print(*self.field, sep='\n')


class Play():
    def play_game(self) -> None:
        chosen = Game().greetings()
        chosen_side = Game().choose_side(chosen)
        player_sign, computer_sign = Game().signs_definition(chosen_side)
        first_turn = Game().first_turn(chosen_side)

        while Game().end == False:
            Game().end_game()
            if first_turn:
                Game().draw_field()
                Game().player_turn(player_sign)
                Game().draw_field()
                Game().computer_turn(computer_sign)
            else:
                Game().draw_field()
                Game().computer_turn(computer_sign)
                Game().draw_field()
                Game().player_turn(player_sign)


if __name__ == '__main__':
    Play().play_game()
