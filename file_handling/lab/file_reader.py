file = open('numbers.txt')

# Variant 1
# the_sum = 0
# for line in file:
#     the_sum += int(line)
#
# print(the_sum)

# Variant 2

print(
    sum(
        [int(line) for line in file]
    )
)
