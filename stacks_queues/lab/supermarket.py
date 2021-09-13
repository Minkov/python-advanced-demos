import sys
from collections import deque
from io import StringIO

input1 = """George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End"""

input2 = """Anna
Emma
Alexander
End"""

sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

queue = deque()

while True:
    command = input()
    if command == 'End':
        print(f'{len(queue)} people remaining.')
        break
    elif command == 'Paid':
        while queue:
            # print(queue.pop())
            print(queue.popleft())
    else:
        # queue.appendleft(command)
        queue.append(command)

ll = []

while True:
    command = input()
    if command == 'End':
        print(f'{len(ll)} people remaining.')
        break
    elif command == 'Paid':
        for x in ll:
            print(x)
        ll = []
    else:
        ll.append(command)
