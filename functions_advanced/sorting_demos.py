# values = [1, -1, 2, 1, 3, 4, 5, 6, 1, 2, 3, 4, -100]

# print(values)
# print(sorted(values))  # new list, that is sorted
# print(values)
# values.sort()  # sorts the list
# print(values)

print(
    [1, 5, -1, -5, -8, 2, 7, 4, -100]
)

print(
    sorted(
        [1, 5, -1, -5, -8, 2, 7, 4, -100]
    )
)

print(
    sorted(
        [1, 5, -1, -5, -8, 2, 7, 4, -100],
        reverse=True,
    )
)

print(
    sorted(
        [1, 5, -1, -5, -8, 2, 7, 4, -100],
        key=lambda x: (x % 5, x)
    )
)

print(
    sorted(
        [1, 5, -1, -5, -8, 2, 7, 4, -100],
        key=lambda x: (x % 5, -x)
        # -100, -5, 5
        #  100,  5, -5
    )
)

print(
    sorted(
        [1, 5, -1, -5, -8, 2, 7, 4, -100],
        key=lambda x: (x % 5, x),
        reverse=True,
    )
)


def order_by_remainder_5(x):
    return (x % 5, x)


print(
    sorted(
        [1, 5, -1, -5, -8, 2, 7, 4, -100],
        key=order_by_remainder_5,
    )
)

print(
    sorted(
        ['Pesho', 'Doncho', 'Gosho', 'Maria', ]
    )
)

print(
    sorted(
        [(1, 7), (-1, 3), (1, 4)]
    )
)

dd = {
    'Peter': 21,
    'George': 18,
    'John': 45,
}

print(dd)
print(dd.items())
print(sorted(dd))
print(
    sorted(
        dd.items()
    )
)
print(
    sorted(
        dd.items(),
        key=lambda x: x[1],
    )
)

print(
    sorted(
        dd.items(),
        key=lambda x: x[1],
        reverse=True,
    )
)
