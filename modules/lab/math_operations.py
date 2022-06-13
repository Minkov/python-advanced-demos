def perform_operation(sign, *args):
    if sign == '+':
        return sum(args)
    elif sign == '*':
        result = 1
        for x in args:
            result *= x
        return result
