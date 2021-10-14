'''
https://judge.softuni.org/Contests/Practice/Index/2812#0
'''
from collections import deque


def are_fireworks_enough(fireworks):
    return all(x >= 3 for x in fireworks.values())


def mix_fireworks(firework_effects, explosive_powers):
    firework_effects_queue = deque([x for x in firework_effects if x > 0])
    explosive_powers_stack = [x for x in explosive_powers if x > 0]

    fireworks = {
        'palm': 0,
        'willow': 0,
        'crossette': 0,
    }

    while firework_effects_queue \
            and explosive_powers_stack \
            and not are_fireworks_enough(fireworks):
        firework_effect = firework_effects_queue.popleft()  # firework_effects_queue[0]
        explosive_power = explosive_powers_stack.pop()  # explosive_powers_stack[-1]

        current_sum = firework_effect + explosive_power

        if current_sum % 3 == 0 and current_sum % 5 == 0:
            fireworks['crossette'] += 1
        elif current_sum % 3 == 0:
            fireworks['palm'] += 1
        elif current_sum % 5 == 0:
            fireworks['willow'] += 1
        else:
            #  firework_effect - 1 > 0 => firework_effect > 1
            if firework_effect > 1:
                firework_effects_queue.append(firework_effect - 1)
            explosive_powers_stack.append(explosive_power)

    return (fireworks, firework_effects_queue, explosive_powers_stack)


def print_fireworks(fireworks, firework_effects, explosive_powers):
    if firework_effects:
        print(f'Firework Effects left: {", ".join(str(x) for x in firework_effects)}')
    if explosive_powers:
        print(f'Explosive Power left: {", ".join(str(x) for x in explosive_powers)}')
    print(f'''Palm Fireworks: {fireworks['palm']}
Willow Fireworks: {fireworks['willow']}
Crossette Fireworks: {fireworks['crossette']}
''')


def print_success(fireworks, firework_effects, explosive_powers):
    print(f'Congrats! You made the perfect firework show!')
    print_fireworks(fireworks, firework_effects, explosive_powers)


def print_fail(fireworks, firework_effects, explosive_powers):
    print('Sorry. You can\'t make the perfect firework show.')
    print_fireworks(fireworks, firework_effects, explosive_powers)


fe = [int(x) for x in input().split(', ')]
ep = [int(x) for x in input().split(', ')]

(fireworks, remaining_firework_effects, remaining_explosive_powers) = mix_fireworks(fe, ep)

if are_fireworks_enough(fireworks):
    print_success(fireworks, remaining_firework_effects, remaining_explosive_powers)
else:
    print_fail(fireworks, remaining_firework_effects, remaining_explosive_powers)

'''
FE: 5, 6, 4, 16, 11, 5, 30, 2, 3, 27
EP: 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22

check each sum for division by 3 and 5

Type1(%3): 4
Type2(%5): 3
Type3(%3&%5): 3

5 + 22 = 27 % 3  == 0
Type 1 Found!

FE: 6, 4, 16, 11, 5, 30, 2, 3, 27
EP: 1, 13, 5, 3, -7, 32, 19, 3, 5, 7

6 + 7 = 13
No type found!

FE: 4, 16, 11, 5, 30, 2, 3, 27, 5
EP: 1, 13, 5, 3, -7, 32, 19, 3, 5, 7

4 + 7 = 11
No type found!


FE: 16, 11, 5, 30, 2, 3, 27, 5, 3
EP: 1, 13, 5, 3, -7, 32, 19, 3, 5, 7

16 + 7 = 23
No type found!

FE: 11, 5, 30, 2, 3, 27, 5, 3, 15
EP: 1, 13, 5, 3, -7, 32, 19, 3, 5, 7

11 + 7 = 18 % 3 == 0
Type 1 found!

FE: 5, 30, 2, 3, 27, 5, 3, 15
EP: 1, 13, 5, 3, -7, 32, 19, 3, 5

5+5=10 % 5 == 0
Type 2 found!


FE: 30, 2, 3, 27, 5, 3, 15
EP: 1, 13, 5, 3, -7, 32, 19, 3

30+3=33 % 3==0
Type 1 found!

FE: 2, 3, 27, 5, 3, 15
EP: 1, 13, 5, 3, -7, 32, 19

2+19 = 21%3==0
Type 1 found!

FE: 3, 27, 5, 3, 15
EP: 1, 13, 5, 3, -7, 32

3+32=35%5==0

Type 2 found

FE: 27, 5, 3, 15
EP: 1, 13, 5, 3

27+3 =30 % (3, 5)

Type 3 found

FE: 5, 3, 15
EP: 1, 13, 5

5 + 5 = 10 % 5 ==0
Type 2 found

FE: 3, 15
EP: 1, 13

3+13=16

No type found

FE: 15, 2
EP: 1, 13

15 + 13 = 28
No type found

FE: 2, 14
EP: 1, 13

2+13=15 % (3,5)==0
Type 3 found


FE: 14
EP: 1
14+1=15 %(3,5)==0

Type 3 found
'''
