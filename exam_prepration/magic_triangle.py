'''
https://judge.softuni.org/Contests/Practice/Index/2720#2
'''

ready = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]]


def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for row_index in range(2, n):
        triangle.append([])
        triangle[-1].append(1)
        for column_index in range(1, row_index):
            left = triangle[row_index - 1][column_index - 1]
            right = triangle[row_index - 1][column_index]
            triangle[-1].append(left + right)
        triangle[-1].append(1)
        # for column_index in range(row_index + 1):
        #     left = triangle[row_index - 1][column_index - 1] if column_index > 0 else 0
        #     right = triangle[row_index - 1][column_index] if column_index < row_index else 0
        #     triangle[-1].append(left + right)
    return triangle


# for i in range(2, 10):
#     print(get_magic_triangle(i))

print(get_magic_triangle(5))

print(ready)
