from time import time

ss1 = []

ss2 = []

n = 100000

start = time()
for i in range(n):
    ss1.append(i)
end = time()

print(f'Executed in ${end - start}')
print('Executed in ' + (end - start))

start = time()
for i in range(n):
    ss2.insert(0, i)
end = time()
print(f'Executed in {end - start}')
