def f(*args, **kwargs):
    print(' ------- ')
    print(args)
    print(kwargs)
    print(' ------- ')


f(1, 2, 3)
f(x=1, y=2, z=3)
f(1, 2, 3, y=4)
f()


def f2(x, *args, **kwargs):
    print(f'x={x}, args={args}, kwargs={kwargs}')


f2(1)
f2(1, 2)
f2(1, 2, 3)

f2(x=11)
f2(1, 2, 3, 4, 5, y=12)
