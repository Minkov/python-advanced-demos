'''
   0 1 2 3 4 5 6 7
0: - - - - - - b -
1: - - - - - - - -
2: - - - - - - - -
3: - - - - - - - -
4: - - - - - - - -
5: - w - - - - - -
6: - - - - - - - -
7: - - - - - - - -

# Best solution:

white - (6, 2)
black - (1, 6)

if abs(col(white) - col(black)) > 1:
   fastest to last row
else:
    distance = abs(row(white) - row(black))
    if distance is odd:
        black wins
    else:
        white wins

# Solution with matrix:
'''
import sys
from io import StringIO

test_input_1 = '''
- - - - - - b -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
'''.strip()

test_input_2 = '''
- - b - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- w - - - - - -
- - - - - - - -
- - - - - - - -
'''.strip()

test_input_3 = '''
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
b - - - - - - -
- w - - - - - -
- - - - - - - -
'''.strip()

sys.stdin = StringIO(test_input_1)
# sys.stdin = StringIO(test_input_2)
sys.stdin = StringIO(test_input_3)


def find_player_position(matrix, player):
    for (row_index, row) in enumerate(matrix):
        if player in row:
            return (row_index, row.index(player))

    return (None, None)


def get_chess_position(row, column):
    row_names = [8, 7, 6, 5, 4, 3, 2, 1]
    columns_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return row_names[row], columns_names[column]


ROWS_COUNT = 8
COLUMNS_COUNT = 8

matrix = [input().split(' ') for _ in range(ROWS_COUNT)]

current_player = 'w'
other_player = 'b'
current_player_position = find_player_position(matrix, 'w')
other_player_position = find_player_position(matrix, 'b')
current_delta = -1
other_delta = +1

is_capture = False
is_queen = False

while not is_queen and not is_capture:
    (current_player_row, current_player_column) = current_player_position
    (other_player_row, other_player_column) = other_player_position

    current_player_row += current_delta
    current_player_position = (current_player_row, current_player_column)

    if current_player_row == other_player_row \
            and abs(current_player_column - other_player_column) == 1:
        is_capture = True
        current_player_position = (current_player_row, other_player_column)
    elif current_player_row in (0, ROWS_COUNT - 1):
        is_queen = True
    else:
        current_player_position, other_player_position = other_player_position, current_player_position
        current_delta, other_delta = other_delta, current_delta
        current_player, other_player = other_player, current_player

player = 'White' if current_player == 'w' else 'Black'
(row_name, column_name) = get_chess_position(*current_player_position)
position_name = f'{column_name}{row_name}'

if is_capture:
    print(f'Game over! {player} win, capture on {position_name}.')

if is_queen:
    print(f'Game over! {player} pawn is promoted to a queen at {position_name}.')
