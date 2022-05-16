from collections import deque

'''
queue

loop:
    add input to queue
    if input is 'Paid':
        print and empty queue
    if input is 'End':
        print remaining
'''

queue = deque()

while True:
    command = input()
    if command == 'End':
        print(f'{len(queue)} people remaining.')
        break
    elif command == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)
