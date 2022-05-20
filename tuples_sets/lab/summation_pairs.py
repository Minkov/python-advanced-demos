'''
Sum of 2

With ordered values:
1 2 2 2 3 3 4 5
target=4
p1=1
p2=5

Algorithm:
current_sum = p1 + p2
current_sum <> target
if current_sum ==  target:
    Great!
elif current_sum < target:
    move p1 right
else: # current_sum > target
    move p2 left

# 1
p1=1
p2=5
values = 1 2 2 2 3 3 4 5
p1+p2 <> target
# 2
p1=1
p2=4
values = 1 2 2 2 3 3 4 5
p1+p2 <> target
# 3
p1=1
p2=3
values = 1 2 2 2 3 3 4 5


Without ordered values:
values=1 5 4 2 2 3 1 3 2
target=4

targets=[
algorithms:
    check if current_value is in targets:
        if it is:
            Great!
        else:
            add target-current_value to targets

# 1
values=[1, 5, 4, 2, 2, 3, 1, 3, 2]
targets={
current_value=1

# 2
values=[1, 5, 4, 2, 2, 3, 1, 3, 2]
targets={3,
current_value=5

# 3
values=[1, 5, 4, 2, 2, 3, 1, 3, 2]
targets={3, -1,
current_value=4

# 4
values=[1, 5, 4, 2, 2, 3, 1, 3, 2]
targets={3, -1, 0,
current_value=2

# 5
values=[1, 5, 4, 2, 2, 3, 1, 3, 2]
targets={3, -1, 0, 2,
current_value=2
'''
import time
from random import shuffle

ll = list(range(1024 * 8))
shuffle(ll)

target = 8
targets = set()
values_map = {}

start = time.time()
for value in ll:
    if value in targets:
        p1 = value
        p2 = values_map[value]
        print(f'{p2} + {p1} = {target}')
    else:
        targets.add(target - value)
        values_map[target - value] = value

end = time.time()
print(f'{end - start} s')

target = 8

start = time.time()
for i1 in range(len(ll)):
    for i2 in range(i1 + 1, len(ll)):
        p1 = ll[i1]
        p2 = ll[i2]
        if p1 + p2 == target:
            print(f'{p1} + {p2} = {target}')

end = time.time()
print(f'{end - start} s')
