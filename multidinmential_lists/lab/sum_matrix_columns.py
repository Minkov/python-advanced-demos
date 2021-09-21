import sys
from io import StringIO

test_input1 = '''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''

sys.stdin = StringIO(test_input1)


def read_matrix():
    n, m = [int(x) for x in input().split(', ')]

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(' ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()

n = len(matrix)
m = len(matrix[0])

column_sums = [0] * m
#
# for r in range(n):
#     for c in range(m):
#         value = matrix[r][c]
#         column_sums[c] += value

for c in range(m):
    for r in range(n):
        value = matrix[r][c]
        column_sums[c] += value

[print(x) for x in column_sums]
