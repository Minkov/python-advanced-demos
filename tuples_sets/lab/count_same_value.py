'''
occurrences_dict
loop values:
    occurrences_dict[value] += 1
'''

# numbers_string = '-2.5 4 3 -2.5 -5.54 4 3 3 -2.5 3'
# numbers_string = '2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3'

numbers_string = input()

occurrence_counts = {}
# No such thing as tuple comprehension, this is generator
numbers = [float(x) for x in numbers_string.split(' ')]

for number in numbers:
    # Not the best solution
    # if number in occurrence_counts:
    #     occurrence_counts[number] += 1
    # else:
    #     occurrence_counts[number] = 1
    if number not in occurrence_counts:
        occurrence_counts[number] = 0

    occurrence_counts[number] += 1

for number, count in occurrence_counts.items():
    print(f'{number:.1f} - {count} times')
