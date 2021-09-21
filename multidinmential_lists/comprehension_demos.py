matrix = [
    [1, 2, 3, 4, 5],
    [-2, -3, -4, -5, -6],
    [100, 200, 300, 400, 500],
    [1, 101, 1001, 10001, 100001],
]

expected_result = [
    1, 2, 3, 4, 5, -2, -3, -4, -5, -6, 100, 200, 300, 400, 500, 1, 101, 1001, 10001, 100001
]

ll = [x for row in matrix for x in row]
#
# print(ll)
# print(expected_result)

ll2 = []
ll2_copy = ll2
for row in matrix:
    ll2 += row
    # ll2.extend(row)

print(ll2_copy)
print(ll2)
