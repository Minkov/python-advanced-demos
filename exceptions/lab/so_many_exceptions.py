import sys
from io import StringIO


def find_sum(numbers_list):
    result = 1
    numbers_list_count = len(numbers_list)
    for i in range(numbers_list_count):
        number = numbers_list[i]
        if number <= 5:
            result *= number
        elif number <= 10:
            result /= number
    return result


print(find_sum([1, 4, 5]), 20)
print(find_sum([4, 5, 6, 1, 3]), 10)
# 4 * 5 / 6 * 1 * 3 = 4*3*5/6 = 10
print(find_sum([2, 5, 10]), 1)
#
print(find_sum(list(range(1, 12))), 0.003968253968253968)
# print(find_sum(input().split(', ')))
