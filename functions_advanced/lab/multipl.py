def multiply(*args):
    product = 1

    for v in args:
        product *= v

    return product


print(multiply(1))
print(multiply(1, 2, 3))
print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9))
