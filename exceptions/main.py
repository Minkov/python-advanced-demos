# DivisionByZero exception
def avg(numbers):
    # Fixes the case with empty list
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


#
# x = 0  # very complicated formula
#
# print(5 / x)

print(avg([1, 2, 3]))
print(avg([]))

# Name Exception
# x = 5
# print(x)

# Index exception
# Solution: check the index before call

# ll = [1]
# print(ll[1])
# print(ll[-2])

# Key exception
# Solution: check whether key is in dict
dd = {
    'k1': 'v1',
    'k2': 'v2',
}

if 'k3' in dd:
    print(dd['k3'])

# Type Exception
# Solution: Ensure the type is correct
# print(', '.join(['p', 2, 3]))
print(', '.join(str(x) for x in ['p', 2, 3]))

# print(sum([1, 2, '3']))
print(sum(int(x) for x in [1, 2, '3']))

# print('s' * 5.3)

# Value Error

print(int(1))
print(int(3.14))
print(int('1'))

print(int('aa', 36))
# 10*16 + 10 = 170 -> base  16
# 10*36 + 10 = 370 -> base 36
# print(int({}))

# Raising exceptions

# raise IndexError('My index is out of range')
te = TypeError('The type is incorrect')


# raise te
#
# raise Type('The type is incorrect')
# print(te)


# Custom exceptions

class ValueTooSmallError(Exception):
    def __init__(self, min_value):
        super().__init__(f'The must be greater or equal to {min_value}')

#
# raise ValueTooSmallError(5)
