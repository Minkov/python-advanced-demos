import sys
from io import StringIO

test_input1 = '''2
1, 2, 3
4, 5, 6
'''


# sys.stdin = StringIO(test_input1)


def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()

print(
    [x for row in matrix for x in row]
)
