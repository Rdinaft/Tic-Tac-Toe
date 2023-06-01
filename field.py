from enums import Signs


def create_field(field_size: int) -> list[list[Signs | None]]:
    game_board_list = [[None] * field_size for i in range(field_size)]
    return game_board_list


def draw_field(field: list[list[Signs | None]]) -> None:
    for line in field:
        print(line)
