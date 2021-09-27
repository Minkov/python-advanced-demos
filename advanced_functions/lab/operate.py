def operate(operator, *args):
    if operator == '+':
        return sum(args)
    elif operator == '*':
        return None


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
