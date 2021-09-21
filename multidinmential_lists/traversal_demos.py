# matrix = [
#     [7, 1, 3, 3, 2, 1],  # row 0
#     [1, 3, 9, 8, 5, 6],  # row 1
#     [4, 6, 7, 9, 1, 0],  # row 2
# ]
#
# print(matrix[1])
#
# ll = matrix[1]
# print(ll[3])
#
# print(matrix[1][3])
# print(matrix[2][2])
# print(matrix[-1][-1])
# print(matrix[1][5])
# print(matrix[1][-1])
#
# cube = [
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#     ],
#     [
#         [-1, -2, -3],
#         [-4, -5, -6],
#     ],
# ]
#
# print(cube[1][1][1])
# print(cube[1][0][1])
# print(cube[0][1][1])

matrix = [
    [7, 1, 3, 3, 2, 1],  # row 0
    [1, 3, 9, 8, 5, 6],  # row 1
    [4, 6, 7, 9, 1, 0],  # row 2
]

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index])):
        value = matrix[row_index][column_index]
        print(f'{value}{row_index, column_index}', end=', ')
    print()

print(matrix[2][3])
matrix[2][3] = -17
print(matrix[2][3])
