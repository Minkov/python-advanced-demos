ll = [1, 2, 3, 4, 5, 6, 7]

ll2 = []
for v in ll:
    ll2.append(v + 1)

print(ll)
print(ll2)

ll3 = [v + 1 for v in ll]
print(ll3)

mm = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

print(mm)
print(
    # [v + 1 for v in ll]
    # a new list          for each list in MD list
    # nested comprehensions
    [[v + 1 for v in row] for row in mm]
)

print(
    # MD comprehension
    # Flattening comprehension
    [
        v + 1
        for row in mm
            for v in row
    ]
)
