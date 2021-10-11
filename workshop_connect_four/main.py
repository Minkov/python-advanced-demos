import sys
from io import StringIO

test_input = '''1
1
3
3
4
4
2
2
'''

sys.stdin = StringIO(test_input)


def get_player_choice(player):
    choice = input(f'Player {player}, please choose a column\n')
    return int(choice) - 1


def apply_player_choice(board, player_choice, player):
    row_index = 0
    while row_index < len(board) and board[row_index][player_choice] is None:
        row_index += 1

    board[row_index - 1][player_choice] = player
    return (row_index - 1, player_choice)


def get_right_win_condition_values(board, row_index, column_index, max_column_index):
    right_win_condition = [board[row_index][c] for c in range(column_index, max_column_index)]
    return right_win_condition


def get_left_win_condition_values(board, row_index, column_index, min_column_index):
    left_win_condition = [board[row_index][c] for c in range(column_index, min_column_index, -1)]
    return left_win_condition


def get_up_win_condition_values(board, row_index, column_index, min_row_index):
    values = [board[r][column_index] for r in range(row_index, min_row_index, -1)]
    return values


def get_down_win_condition_values(board, row_index, column_index, max_row_index):
    values = [board[r][column_index] for r in range(row_index, max_row_index)]
    return values


def get_down_right_win_condition_values(board, row_index, column_index, max_row_index, max_column_index):
    values = []
    max_d = min(
        max_row_index - row_index,
        max_column_index - column_index,
    )
    for d in range(max_d):
        r = row_index + d
        c = column_index + d
        values.append(board[r][c])
    return values


def get_down_left_win_condition_values(board, row_index, column_index, max_row_index, min_column_index):
    values = []
    max_d = min(
        max_row_index - row_index,
        abs(min_column_index - column_index),
    )
    for d in range(max_d):
        r = row_index + d
        c = column_index - d
        values.append(board[r][c])
    return values


def get_up_right_win_condition_values(board, row_index, column_index, min_row_index, max_column_index):
    values = []
    max_d = min(
        abs(min_row_index - row_index),
        max_column_index - column_index,
    )
    for d in range(max_d):
        r = row_index - d
        c = column_index + d
        values.append(board[r][c])
    return values


def get_up_left_win_condition_values(board, row_index, column_index, min_row_index, min_column_index):
    values = []
    max_d = min(
        abs(min_row_index - row_index),
        abs(min_column_index - column_index),
    )
    for d in range(max_d):
        r = row_index - d
        c = column_index - d
        values.append(board[r][c])
    return values


def check_win_condition(board, row_index, column_index, win_count):
    min_column_index = max(column_index - win_count, -1)
    max_column_index = min(column_index + win_count, len(board[row_index]))

    min_row_index = max(row_index - win_count, -1)
    max_row_index = min(row_index + win_count, len(board))

    right_win_condition_values = get_right_win_condition_values(
        board,
        row_index,
        column_index,
        max_column_index
    )
    left_win_condition_values = get_left_win_condition_values(
        board,
        row_index,
        column_index,
        min_column_index
    )
    up_win_condition_values = get_up_win_condition_values(
        board,
        row_index,
        column_index,
        min_row_index
    )
    down_win_condition_values = get_down_win_condition_values(
        board,
        row_index,
        column_index,
        max_row_index
    )

    up_left_condition_values = get_up_left_win_condition_values(
        board,
        row_index,
        column_index,
        min_row_index,
        min_column_index
    )
    up_right_condition_values = get_up_right_win_condition_values(
        board,
        row_index,
        column_index,
        min_row_index,
        max_column_index
    )
    down_left_condition_values = get_down_left_win_condition_values(
        board,
        row_index,
        column_index,
        max_row_index,
        min_column_index
    )
    down_right_condition_values = get_down_right_win_condition_values(
        board,
        row_index,
        column_index,
        max_row_index,
        max_column_index
    )

    possible_win_condition_values = [
        right_win_condition_values,
        left_win_condition_values,
        up_win_condition_values,
        down_win_condition_values,
        up_right_condition_values,
        up_left_condition_values,
        down_left_condition_values,
        down_right_condition_values,
    ]

    for values in possible_win_condition_values:
        if len(values) == win_count and len(set(values)) == 1:
            return True

    return False


def is_player_choice_valid(board, player_choice):
    is_column_index_valid = 0 <= player_choice < len(board[0])
    has_column_space = is_column_index_valid \
                       and board[0][player_choice] is None
    return is_column_index_valid and has_column_space


def play(board):
    current_player, other_player = 1, 2

    while True:
        player_choice = get_player_choice(current_player)
        if not is_player_choice_valid(board, player_choice):
            print('Wrong column, try again!')
            continue
        row_index, column_index = apply_player_choice(board, player_choice, current_player)
        if check_win_condition(board, row_index, column_index, 4):
            print(f'Player {current_player} wins!')
            break

        # End of player's turn
        print_board(board)
        current_player, other_player = other_player, current_player


def create_board(rows_count, columns_count):
    return [[None] * columns_count for _ in range(rows_count)]


def print_board(board):
    def get_value(value):
        if value is None:
            return 0
        return value

    for row in board:
        print([get_value(x) for x in row])


board = create_board(6, 7)

play(board)
