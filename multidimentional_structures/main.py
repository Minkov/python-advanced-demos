# single-dimensional list
ll = [1, 2, 3, 4, 5, 6, 7,]

print(ll)
ll.append(-11)
print(ll)
ll.pop()
print(ll)

# two-dimensional list
## list of lists
mm = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
]


print(mm)
mm.append([-11])
print(mm)
mm.pop()
print(mm)

print(ll[1])
print(mm[1])


# three-dimensional list
## list of lists of lists
cc = [
    [ # 0
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5],
    ],
    [ # 1
        [4, 5, 6],
        [5, 6, 7],
        [6, 7, 8],
    ],
    [ # 2
        [7, 8, 9],
        [8, 9, 10],
        [9, 10, 11],
    ],
]