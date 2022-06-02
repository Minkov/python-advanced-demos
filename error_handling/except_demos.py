import random


def try_raise_exception():
    value = random.random()
    if value < 0.3:
        raise ValueError('Invalid value')
    elif value < 0.7:
        raise TypeError('Invalid type')


for i in range(10):
    try:
        try_raise_exception()
        print(f'Try {i}: No exception')
    except (ValueError, TypeError) as e:
        print(f'Try {i}: Yes exception ({type(e).__name__}: {e})')


for i in range(10):
    try:
        try_raise_exception()
        print(f'Try {i}: No exception')
    except ValueError as e:
        print(f'Try {i}: Value exception')
    except TypeError:
        print(f'Try {i}: Type exception')


