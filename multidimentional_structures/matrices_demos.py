# Create list `n` zeros

n = 5

ll = []
for _ in range(n):
    x = 0
    ll.append(x)

print(ll)

# create NxM matrix of zeros

n = 5
m = 3
mm = []

for _ in range(n):
    ll = []
    for _ in range(m):
        ll.append(0)
    mm.append(ll)

print(mm)

mm = []

for i in range(n):
    ll = []
    for j in range(m):
        ll.append(i * n + j)
    mm.append(ll)

print(mm)
