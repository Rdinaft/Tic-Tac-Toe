def get_winner_per_row(
    sign_dict: dict[str, str], field: list[list[str | None]], num_of_lines: int
) -> str | None:
    for participant in sign_dict:
        for line in range(num_of_lines):
            if field[line] == [sign_dict[participant]] * len(field[line]):
                return participant
    return None


def get_winner_per_column(
    sign_dict: dict[str, str], field: list[list[str | None]], num_of_lines: int
) -> str | None:
    for participant in sign_dict:
        for column in range(num_of_lines):
            if [field[line][column] for line in range(num_of_lines)] == [
                sign_dict[participant]
            ] * len(field[column]):
                return participant
    return None


def get_winner_per_diagonal(
    sign_dict: dict[str, str], field: list[list[str | None]], num_of_lines: int
) -> str | None:
    for participant in sign_dict:
        if [field[line][line] for line in range(num_of_lines)] == [
            sign_dict[participant]
        ] * len(field[num_of_lines - 1]):
            return participant
        elif [field[num_of_lines - 1 - line][line] for line in range(num_of_lines)] == [
            sign_dict[participant]
        ] * len(field[num_of_lines - 1]):
            return participant
    return None


def check_for_tie(field: list[list[str | None]]) -> bool:
    if None not in sum(field, []):
        return True
    return False


def spot_the_winner(
    sign_dict: dict[str, str], field: list[list[str | None]], num_of_lines: int
) -> str | None:
    ending_conditions = [
        get_winner_per_row(sign_dict, field, num_of_lines),
        get_winner_per_column(sign_dict, field, num_of_lines),
        get_winner_per_diagonal(sign_dict, field, num_of_lines),
    ]
    for winner in ending_conditions:
        if winner is not None:
            return winner
    return "Nobody"
