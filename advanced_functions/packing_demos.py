def add_with_list(numbers):
    return sum(numbers)


def add(x, *args, **kwargs):
    print(' -- New call --')
    print(f'x={x}')
    print(f'args={args}')
    print(f'kwargs={kwargs}')
    return sum(args) + sum(kwargs.values())


print(add(1, 2, 3))

print(add(x=1, y=2, z=3))

print(add(y=1, z=3, x=2))

print(add(x=1, z=3, y=5))

print(add(1, 2, z=5))

print(add(1))
