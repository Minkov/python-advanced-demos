def perform_operation(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '/':
        if number2 == 0:
            raise ValueError('In division, number 2 must not be equal to 0')
        return number1 / number2
    elif operation == '*':
        return number1 * number2
    elif operation == '^':
        return number1 ** number2
    else:
        raise ValueError('Operation must be one of the following: "+", "-", "*", "/", "^",')
