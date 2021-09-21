# ll = [1, 2, 3, 4]
#
# print(ll[2])
#
list_of_strings = [
    'Doncho',
    'Pesho',
    'Gosho',
]
print(list_of_strings)
# # list of lists of characters

list_of_lists = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
]
# # list of lists of numbers
#
# print(list_of_strings[2])
# print(list_of_lists[2])


[
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

n = 5  # rows_count
m = 4  # columns_count

# Version 1
# matrix_of_zeroes = []
#
# for _ in range(n):
#     row = []
#     for _ in range(m):
#         row.append(0)
#
#     matrix_of_zeroes.append(row)
#
# print(matrix_of_zeroes)
#
# for row in matrix_of_zeroes:
#     print(row)

# Version 2
# matrix_of_zeroes = []
#
# for _ in range(n):
#     matrix_of_zeroes.append([0] * m)
#
# print(matrix_of_zeroes)
#
# for row in matrix_of_zeroes:
#     print(row)

# # Version 3
# matrix_of_zeroes = [[0] * m for _ in range(n)]
# # matrix_of_zeroes = [[0] * m] * n  # Don't do that
#
# print(matrix_of_zeroes)
#
# for row in matrix_of_zeroes:
#     print(row)


# Version 1
# matrix_of_numbers = []

# for _ in range(n):
#     row = []
#     for i in range(m):
#         row.append(i)
#
#     matrix_of_numbers.append(row)

matrix_of_numbers = [[x for x in range(m)] for _ in range(n)]

print(matrix_of_numbers)

for row in matrix_of_numbers:
    print(row)
