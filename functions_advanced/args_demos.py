def f1(args):
    print(args)


def f2(*args):
    print(args)

print(' --- f1() ---')
f1(1)
f1([1, 2, 3])
f1({'x': 1, 'y': 2})
f1({1, 2, 3})

print(' --- f2() ---')
f2(1)
f2([1, 2, 3])
f2({'x': 1, 'y': 2})
f2({1, 2, 3})
f2(1, 2)
f2(1, 2, 3)
f2()
