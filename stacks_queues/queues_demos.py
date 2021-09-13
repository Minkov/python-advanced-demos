from collections import deque
from time import time

qq_slow = []

qq = deque()
n = 100000

start = time()
for i in range(n):
    # qq_slow.append(i)
    qq_slow.insert(0, i)

while len(qq_slow) > 0:
    # x = qq_slow.pop(0)
    x = qq_slow.pop()

end = time()
print(f' -- Slow -- Executed in {end - start}')

start = time()
for i in range(n):
    # qq.append(i)
    qq.appendleft(i)

while len(qq) > 0:
    # x = qq.popleft()
    x = qq.pop()
    y = qq.pop

end = time()
print(f' -- Fast -- Executed in {end - start}')
