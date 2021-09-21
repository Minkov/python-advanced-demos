import sys
from io import StringIO

test_input_1 = '''3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
'''

sys.stdin = StringIO(test_input_1)


def read_matrix():
    n, m = [int(x) for x in input().split(', ')]
    # n, m = map(int, input().split(', '))
    # n, m = list(map(int, input().split(', '))) # Don't do this

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()
n = len(matrix)
m = len(matrix[0])
the_sum = 0

for row_index in range(n):
    row = matrix[row_index]
    the_sum += sum(row)
    # for column_index in range(m):
    #     the_sum += row[column_index]
# the_sum2 = sum(sum(row) for row in matrix) # Short variant

print(the_sum)
print(matrix)
