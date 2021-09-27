def multiply(*args):
    if not args:
        return None

    product = 1
    for x in args:
        product *= x

    return product


print(multiply())
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
