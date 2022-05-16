from collections import deque

q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(q)
for _ in range(4):
    q.append(q.popleft())

print(q)

q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(q)
q.rotate(5)
print(q)

q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(q)
q.rotate(-4)
print(q)
