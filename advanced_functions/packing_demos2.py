def f1(x, y, z):
    print(x, y, z)


def f2(x, *args, **kwargs):
    print(x)
    f1(*args, **kwargs)


print(f2(1, 2, 3, 4))
print(f2(1, 2, 3, z=5))
