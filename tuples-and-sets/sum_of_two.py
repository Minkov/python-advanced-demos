ll = [1, 2, 3, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5] * 5
target = 9

# 8, 7, 6, 5,
c = 0
n = len(ll)

for i in range(n):
    for j in range(i + 1, n):
        # print(c)
        c += 1
        if i == j:
            continue
        if ll[i] + ll[j] == target:
            print(ll[i], ll[j])
print(f'Total iterations: {c}')
print(f'Total elements count: {n}')

remainers = set()
c = 0
for x in ll:
    c += 1
    if x in remainers:
        print(x)
    remainers.add(target - x)
print(f'Total iterations: {c}')
print(remainers)

# Break ends at 21:00