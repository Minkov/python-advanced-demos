import sys
from collections import deque
from io import StringIO

input1 = """10
Peter
George
Amy
Alice
Start
2
3
3
3
End
"""

input2 = """2
Peter
Amy
Start
2
refill 1
1
End
"""

# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)

water_quantity = int(input())

people_queue = deque()

while True:
    command = input()
    if command == 'Start':
        break

    people_queue.appendleft(command)

while True:
    command = input()
    if command == 'End':
        break
    elif command.startswith('refill'):
        params = command.split(' ')
        liters_to_add = int(params[1])
        water_quantity += liters_to_add
        # water_quantity += int(command.split(' ')[1])
    else:
        name = people_queue.pop()
        water_wanted = int(command)

        if water_wanted <= water_quantity:
            print(f'{name} got water')
            water_quantity -= water_wanted
        else:
            print(f'{name} must wait')

print(f'{water_quantity} liters left')
