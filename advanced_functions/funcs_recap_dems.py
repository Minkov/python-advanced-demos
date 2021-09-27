def f():
    pass


def add(x, y, z):
    return x + y + z


print(add(1, 2, 3))

print(add(x=1, y=2, z=3))

print(add(y=1, z=3, x=2))

print(add(x=1, z=3, y=5))

print(add(1, 2, z=5))
# print(add(1, 2, x=1)) Does not work
