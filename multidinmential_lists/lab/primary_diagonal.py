import sys
from io import StringIO

test_input1 = '''3
11 2 4
4 5 6
10 8 -12
'''


# sys.stdin = StringIO(test_input1)


def read_matrix():
    n = int(input())

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(' ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()
n = len(matrix)

print(sum([matrix[i][i] for i in range(n)]))

# the_sum = 0
# for i in range(n):
#     the_sum += matrix[i][i]
