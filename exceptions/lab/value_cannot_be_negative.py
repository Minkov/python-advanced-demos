class ValueCannotBeNegative(Exception):
    pass


numbers = [int(input()) for _ in range(5)]

for number in numbers:
    if number < 0:
        raise ValueCannotBeNegative
