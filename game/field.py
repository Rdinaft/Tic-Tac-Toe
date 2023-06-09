from enums import Sign


def create_field(field_size: int) -> list[list[Sign | None]]:
    game_board_list = [[None] * field_size for i in range(field_size)]
    return game_board_list


def draw_field(field: list[list[Sign | None]], sign: Sign) -> None:
    local_field = []
    local_field = local_field + field
    for line in local_field:
        for coordinate in range(len(line)):
            if line[coordinate] == sign.crosses:
                line[coordinate] = sign.crosses.value
            elif line[coordinate] == sign.naughts:
                line[coordinate] = sign.naughts.value
        print(line)
