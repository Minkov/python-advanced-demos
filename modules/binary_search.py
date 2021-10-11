'''
[1, 2, 3, 4, 5, 8, 9, 11, 23, 45]

'''
from time import time


def binary_search_slow_example_only(values, target):
    if not values:
        raise ValueError(f'{target} not in list')
    mid = len(values) // 2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        return mid + 1 + binary_search_slow_example_only(values[mid + 1:], target)
    else:
        return binary_search_slow_example_only(values[:mid], target)


def binary_search(values, target, start_index, end_index):
    if start_index >= end_index:
        raise ValueError(f'{target} not in list')
    mid = (start_index + end_index) // 2
    if values[mid] == target:
        return mid
    elif values[mid] < target:
        return binary_search(values, target, mid + 1, end_index)
    else:
        return binary_search(values, target, start_index, mid)


def measure(action, repeat_count=1):
    start_time = time()
    for i in range(repeat_count):
        action()
    end_time = time()
    print(f' -- Executed in {end_time - start_time} seconds')


def find_all(values):
    s = 0
    for val in values:
        s += binary_search(values, val, 0, len(values))
    return s


def find_all2(values):
    s = 0
    for val in values:
        s += binary_search_slow_example_only(values, val)
    return s


values = [x for x in range(2 ** 15)]

measure(lambda: find_all(values), 5)
measure(lambda: find_all2(values), 5)

'''

ll = [1, 2, 3, 4, 5, 6, 1, 4]

ll2= ll[4:]
same as
ll2=[]
for i in range(4, len(ll)):
  ll2.append(i)



'''
