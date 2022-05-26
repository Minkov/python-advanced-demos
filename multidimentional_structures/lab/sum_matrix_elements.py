n, m = [int(x) for x in input().split(', ')]  # 3, 6

matrix = []

matrix_sum = 0

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
    matrix_sum += sum(row)
print(matrix_sum)
print(matrix)
'''
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
'''
