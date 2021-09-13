"""
George Peter Michael William Thomas
4

[G, P, M, W, T]
1 - [P, M, W, T, G]
2 - [m,w,t,g,p]
3 - [w,t,g,p,m]
4 - [t,g,p,m], [w]

1 - [g,p,m,t]
2 - [p,m,t,g]
3 - [m,t,g,p]
4 - [t,g,p], [w, m]

1 - [g,p,t]
2 - [p,t,g]
3 - [t,g,p]
4 - [g, p], [w, m, t]

"""
import sys
from collections import deque
from io import StringIO

test_input1 = """Tracy Emily Daniel
2"""

test_input2 = """George Peter Michael William Thomas
10"""

test_input3 = """George Peter Michael William Thomas
1"""

# sys.stdin = StringIO(test_input3)

potatoes = input().split(' ')
# potatoes_queue = deque(potatoes)
potatoes_queue = deque()
for p in potatoes:
    potatoes_queue.appendleft(p)

step = int(input())

while potatoes_queue:
    for _ in range(step - 1):
        potatoes_queue.appendleft(potatoes_queue.pop())
    potato_to_remove = potatoes_queue.pop()

    if potatoes_queue:
        print(f'Removed {potato_to_remove}')
    else:
        print(f'Last is {potato_to_remove}')
