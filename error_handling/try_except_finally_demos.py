import random


def try_raise_exception():
    chance = 0.7
    if random.random() < chance:
        raise ValueError('Invalid value')


for i in range(100):
    try:
        # This code **MAY** raise an exception
        try_raise_exception()
        print(f'Try {i}: No exception')
    # `except` is `catch` in `C#`, `Java`, `Js`, etc...
    except ValueError:
        print(f'Try {i}: Value exception!')
    finally:
        print(f'Try {i}: This is finally')

try:
    print(int('qwe'))
finally:
    print('finally')
