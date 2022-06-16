'''

elf, box

if fifteenth time and box * 2 <= elf_energy:
    toys += 0 # 2 toy made and broken
    elf_energy -= 2 * box # used energy
    elf_energy += 0 # does not eat a cookie
    elf goes to the end of the line
if third time and box * 2 <= elf_energy:
    toys += 2 # toy made
    elf_energy -= 2 * box # used energy
    elf_energy += 1 # eats a cookie
    elf goes to the end of the line
if fifth time and box <= elf_energy:
    toys += 0 # toy made and broken
    elf_energy -= box # used energy
    elf_energy += 0 # does not eat a cookie
    elf goes to the end of the line
if box <= elf:
    toys += 1 # toy made
    elf_energy -= box # used energy
    elf_energy += 1 # eats a cookie
    elf goes to the end of the line
if elf_energy < box or (third or fifteenth time and elf_energy < 2 * box):
    leave the box for the next elf
    elf_energy *= 2 # drinks hot chocolate
    elf goes to the end of the line
if elf_energy < 5:
    remove the elf from the line
'''
import sys
from collections import deque
from io import StringIO

'''

elves: 10 16 13 25
boxes: 12 11 8

# Turn 1 - elf 10, box 8
total_energy = 8
toys_count = 1

elves: 16 13 25   (2+1)=3
boxes: 12 11

# Turn 2 - elf 16, box 11
total_energy = 8 + 11 = 19
toys_count = 1 + 1 = 2

elves: 13 25  3  (5+1)=6
boxes: 12

# Turn 3 - elf 13, box 12
total_energy = 19
toys_count = 2

elves: 25  3 6 (13*2)=26
boxes: 12

# Turn 4 - elf 25, box - 12
total_energy = 19 + 12 = 31
toys_count = 3

elves: 3 6 26 (13+1)=14
boxes: (empty)
'''

test_input_1 = '''10 16 13 25
12 11 8
'''

test_input_2 = '''10 14 22 4 5
11 16 17 11 1 8
'''

test_input_3 = '''5 6 7
2 1 5 7 5 3
'''

# sys.stdin = StringIO(test_input_1)
# sys.stdin = StringIO(test_input_2)
# sys.stdin = StringIO(test_input_3)



from collections import deque
elf_energies = deque([int(x) for x in input().split(' ')])
boxes = [int(x) for x in input().split(' ')]
turns_count = 0
total_energy_spent = 0
toys_count = 0

while boxes and elf_energies:
    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()

    if not elf_energies:
        break

    box = boxes.pop()
    elf_energy = elf_energies.popleft()

    turns_count += 1

    toys_to_be_created_count = 1
    energy_to_be_spent = box
    energy_increase_factory = 1

    if turns_count % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spent *= 2
    if turns_count % 5 == 0:
        toys_to_be_created_count = 0
        energy_increase_factory = 0

    if energy_to_be_spent <= elf_energy:
        toys_count += toys_to_be_created_count
        total_energy_spent += energy_to_be_spent
        elf_energies.append(elf_energy - energy_to_be_spent + energy_increase_factory)
    else:
        boxes.append(box)
        elf_energies.append(elf_energy * 2)

print(f'Toys: {toys_count}')
print(f'Energy: {total_energy_spent}')
if elf_energies:
    elves_string = ', '.join(str(x) for x in elf_energies)
    print(f'Elves left: {elves_string}')
if boxes:
    boxes_string = ', '.join(str(x) for x in boxes)
    print(f'Boxes left: {boxes_string}')
