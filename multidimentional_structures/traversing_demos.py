def matrix_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = 0
    for row_index in range(n):
        for column_index in range(m):
            result += matrix[row_index][column_index]
    return result


mm = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

n = len(mm)
m = len(mm[0])

for row_index in range(n):
    print(mm[row_index])
    for column_index in range(m):
        print(mm[row_index][column_index], end=' ')
    print()

print(matrix_sum(mm))
