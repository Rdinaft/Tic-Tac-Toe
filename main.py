'''
Вопрос: иду ли я в правильном направлении? Это пока что примерный скелет
'''

import random


field_coordinates = {'top_left': ' ', 'top_middle': ' ', 'top_right': ' ', 'center_left': ' ', 'center_middle': ' ', 'center_right': ' ', 'bottom_left': ' ', 'bottom_middle': ' ', 'bottom_right': ' '}

def greetings():
    print('Welcome to Tic-Tac-Toe!')
    chosen = input('Choose your side (random, naughts, crosses): ').lower()
    return chosen

def help(chosen):
    if chosen == 'help':
        return print(field_coordinates)

def choose_side(chosen):
    if chosen == 'random':
        chosen_side = random.choice(['naughts', 'crosses'])
    else:
        chosen_side = chosen
    return chosen_side

def player_sign(chosen_side):
    if chosen_side == 'naughts':
        sign = 'O'
    else:
        sign = 'X'
    return sign

def first_turn(chosen_side):
    if chosen_side == 'crosses':
        return True
    else:
        pass

def player_turn(sign):
    move = input('Enter coordinate: ').lower()
    if move in field_coordinates.keys():
        field_coordinates[move] = sign
        return field_coordinates[move]

def draw_field():
    field = [
        [field_coordinates['top_left'], '|', field_coordinates['top_middle'], '|', field_coordinates['top_right']],
        ['---------------------'],
        [field_coordinates['center_left'], '|', field_coordinates['center_middle'], '|', field_coordinates['center_right']],
        ['---------------------'],
        [field_coordinates['bottom_left'], '|', field_coordinates['bottom_middle'], '|', field_coordinates['bottom_right']],
        ]
    return print(*field, sep='\n')


if __name__ == '__main__':
    pass
