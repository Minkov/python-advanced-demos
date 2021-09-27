def add(x, y, z):
    return x + y + z


numbers = (1, 2, 3)

# Variant 1
print(add(numbers[0], numbers[1], numbers[2]))

# Variant 2
a, b, c = numbers
print(add(a, b, c))

# Variant 3
# unpack as positional arguments
print(add(*numbers))

numbers_dict = {
    'x': 1,
    'y': 2,
    'z': 3,
}

# Variant 1
print(add(numbers_dict['x'], numbers_dict['y'], numbers_dict['z']))

# Variant 2
# unpacks named arguments
print(add(**numbers_dict))
