import time

s = []
count = 2 ** 16  # 1024 * 32 ~ 32000
result = 0

start = time.time()
for i in range(count):
    s.append(i)
while s:
    result += s.pop()

end = time.time()
print(end - start)

start = time.time()
for i in range(count):
    s.insert(0, i)
while s:
    result += s.pop(0)

end = time.time()

print(end - start)
