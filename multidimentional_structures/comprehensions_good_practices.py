matrix = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
]

# Wrong
print(
    [[x for x in row if x % 2 == 0] for row in matrix]
)


# Correct

def is_even(number):
    return number % 2 == 0


def get_even(ll):
    return [x for x in ll if is_even(x)]


print(
    [get_even(row) for row in matrix]
)


# Variant 1
def is_special(number):
    return number % 2 == 0 and number > 15 and number % 3 == 2


def get_special(ll):
    return [x for x in ll if is_special(x)]


#  Variant 2
def get_special(ll):
    return [x for x in ll if x % 2 == 0 and x > 15 and x % 3 == 2]


print(
    [get_special(row) for row in matrix]
)
