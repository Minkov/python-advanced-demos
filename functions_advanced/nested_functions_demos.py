def math_operation_factory(operation):
    def add(*args):
        return sum(args)

    def subtract(*args):
        return sum(-x for x in args)

    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    if operation == '+':
        return add
    elif operation == '-':
        return subtract
    elif operation == '*':
        return multiply
    else:
        return None


add = math_operation_factory('+')
subtract = math_operation_factory('-')
print(add(1, 2, 3))
print(add(1, -2, 4))
print(subtract(1, 2, 3))
print(subtract(1, -2, 4))

add1 = math_operation_factory('+')
add2 = math_operation_factory('+')
print(add1 == add2)
print(math_operation_factory == math_operation_factory)


def order_by_factory(type):
    def by_value(x):
        return x

    def by_len(x):
        return len(x)

    if type == 'len':
        return by_len
    else:
        return by_value


print(
    sorted(
        [1, -2, 3, -4, 5, -7],
        key=order_by_factory('value')
    ),
)

print(
    sorted(
        ['Doncho', 'Pesho', 'Gosho'],
        key=order_by_factory('value')
    ),
)

print(
    sorted(
        ['Doncho', 'Pesho', 'Gosho'],
        key=order_by_factory('len')
    ),
)
