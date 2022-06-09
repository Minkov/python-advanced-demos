def build_initial_field(rows_count, columns_count):
    return [[None] * columns_count for _ in range(rows_count)]


def get_cell_value(cell):
    return cell if cell else '*'


def print_field(field):
    [print([get_cell_value(x) for x in row]) for row in field]


def print_winner(player):
    print(f'Player {player} wins!')


def get_player_move(player):
    player_move_str = input(f'Player {player}, please choose a column')
    player_move = int(player_move_str)
    return player_move - 1


def apply_player_move_gen(rows_count, columns_count):
    free_bottom_row_indices = [rows_count - 1] * columns_count

    def apply_player_move_internal(player, player_move, field):
        player_row = free_bottom_row_indices[player_move]
        field[player_row][player_move] = player
        free_bottom_row_indices[player_move] -= 1

        return (player_row, player_move)

    return apply_player_move_internal


def is_win_condition(player, player_row, player_column, field):
    def normalize_player_position_in_direction(field, initial_row, initial_column, direction):
        row_delta, column_delta = direction

        row = initial_row
        column = initial_column
        row_delta *= -1
        column_delta *= -1
        rows_min_boundary = 0
        rows_max_boundary = len(field)
        columns_min_boundary = 0
        columns_max_boundary = len(field[0])

        while rows_min_boundary <= row < rows_max_boundary \
                and columns_min_boundary <= column < columns_max_boundary:
            if field[row][column] != player:
                break
            row += row_delta
            column += column_delta

        if row == initial_row and column == initial_column:
            return row, column

        return row - row_delta, column - column_delta

    def is_win_condition_in_direction(field, initial_row, initial_column, direction):
        row_delta, column_delta = direction
        row, column = normalize_player_position_in_direction(field, initial_row, initial_column, direction)
        rows_boundary = min(len(field), row + 4 * row_delta)
        columns_boundary = min(len(field[0]), column + 4 * column_delta)

        is_row_included = rows_boundary == row
        is_column_included = columns_boundary == column

        counter = 0
        while (row != rows_boundary or is_row_included) \
                and (column != columns_boundary or is_column_included) \
                and player == field[row][column]:
            counter += 1
            row += row_delta
            column += column_delta

        return counter == 4

    directions = [
        (0, 1),  # horizontal
        (1, 0),  # vertical
        (1, 1),  # main diagonal
        (-1, 1),  # secondary diagonal
    ]

    return any(is_win_condition_in_direction(field, player_row, player_column, direction) for direction in directions)


def play(field):
    rows_count = len(field)
    columns_count = len(field[0])
    apply_player_move = apply_player_move_gen(rows_count, columns_count)
    current_player, other_player = 1, 2

    while True:
        player_move = get_player_move(current_player)
        (row, column) = apply_player_move(current_player, player_move, field)
        if is_win_condition(current_player, row, column, field):
            break
        else:
            current_player, other_player = other_player, current_player
        print_field(field)
    print_winner(current_player)


field = build_initial_field(6, 7)
play(field)

#
# print(
#     True,
#     is_win_condition(
#         1,  # player
#         5,  # player row
#         0,  # player column
#         [
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [1, 1, 1, 1, 0, 0, 0],
#         ]
#     ))
#
# print(
#     True,
#     is_win_condition(
#         1,  # player
#         5,  # player row
#         1,  # player column
#         [
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [1, 1, 1, 1, 0, 0, 0],
#         ]
#     ))
#
# print(
#     True,
#     is_win_condition(
#         1,
#         5,  # player row
#         2,  # player column
#         [
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [1, 2, 1, 1, 1, 1, 0],
#         ]
#     ))
#
# print(
#     True,
#     is_win_condition(
#         1,
#         5,  # player row
#         3,  # player column
#         [
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [1, 2, 1, 1, 1, 1, 0],
#         ]
#     ))
# print(
#     True,
#     is_win_condition(
#         1,
#         1,  # player row
#         2,  # player column
#         [
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [1, 2, 2, 1, 1, 1, 0],
#         ]
#     ))
#
# print(
#     True,
#     is_win_condition(
#         1,
#         3,  # player row
#         2,  # player column
#         [
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [1, 2, 2, 1, 1, 1, 0],
#         ]
#     ))
#
# print(
#     True,
#     is_win_condition(
#         1,
#         5,  # player row
#         0,  # player column
#         [
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0, 0],
#         ]
#     ))
#
# print(
#     True,
#     is_win_condition(
#         1,
#         3,  # player row
#         2,  # player column
#         [
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0, 0],
#         ]
#     ))
#
# print(
#     True,
#     is_win_condition(
#         1,
#         1,  # player row
#         0,  # player column
#         [
#             [0, 0, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0, 0],
#             [0, 1, 0, 1, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0],
#             [1, 0, 0, 0, 2, 0, 0],
#         ]
#     ))
#
# print(
#     True,
#     is_win_condition(
#         1,
#         2,  # player row
#         3,  # player column
#         [
#             [0, 0, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0, 0],
#             [0, 1, 0, 1, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0],
#             [1, 0, 0, 0, 2, 0, 0],
#         ]
#     ))
