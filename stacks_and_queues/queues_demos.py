from collections import deque

q = deque()
# Enqueue, push, add
q.append(2)  # appendRight()
q.append(3)  # appendRight()
q.append(4)  # appendRight()
# q.appendleft(3)

print(q)
# Dequeue, pop, remove
q.popleft()
# q.pop()  # popRight()

# Combinations:
# append() + popleft()
# appendleft() + pop()
print(q)

# Peek
print(q[0])

# Count
