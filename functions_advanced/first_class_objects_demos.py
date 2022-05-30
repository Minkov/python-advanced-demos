# def f1():
#     def f2():
#         def f3():
#             print('I am f3')
#
#         print('I am f2')
#         f3()
#
#     print('I am f1')
#     f2()
#
#
# f1()


def math_operation(operation, *args):
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
        return add(*args)
    elif operation == '-':
        return subtract(*args)
    elif operation == '*':
        return multiply(*args)
    else:
        return None


print(math_operation('+', 1, 2, 3, 4))  # 1 + 2 + 3 + 4 = 10
print(math_operation('-', 1, 2, 3, 4))  # - 1 - 2 - 3 - 4= -10
print(math_operation('*', 1, 2, 3, 4))  # 1 * 2 * 3 * 4 = 24
