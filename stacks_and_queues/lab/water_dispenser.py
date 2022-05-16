'''
1. read initial water quantity
2. Read people into a queue
3. loop until 'End':
    if command == 'refill {water}':
        add {water} to water quantity
    else:
        if enough water:
            remove water from water quantity

        remove person from queue
'''

from collections import deque

water_quantity = int(input())
people = deque()
while True:
    command = input()
    if command == 'Start':
        break

    people.append(command)

while True:
    command = input()
    if command == 'End':
        break
    elif command.startswith('refill '):
        params = command.split(' ')
        water_quantity += int(params[1])
    else:
        person = people.popleft()
        water_wanted = int(command)

        if water_wanted <= water_quantity:
            print(f'{person} got water')
            water_quantity -= water_wanted
        else:
            print(f'{person} must wait')

print(f'{water_quantity} liters left')
