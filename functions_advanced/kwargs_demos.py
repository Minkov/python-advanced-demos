def f(**kwargs):  # key-value args
    if 'age' not in kwargs:
        kwargs['age'] = None

    print(kwargs)


f(name='Doncho', age=19)
f(x=1, y=-11)
f(values=[1, 2, 3, 4], pair=(7, 6))
