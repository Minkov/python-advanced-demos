# # Variant 1, import global object
# import random
#
# print(random.randint(1, 5))
# print(random.choice([1, 2, 3]))
#
# # Variant 2, import functions/variables explicitly
# from random import randint, choice
#
# print(randint(1, 5))
# print(choice([1, 2, 3]))

# Variant 2.1

from random import choice as random_choice, randint

import random as r

# import random

choices = [1, 2, 3, 4, 5]
print(r.choice([1, 2, 3]))

# choice([1, 2, 3, ])
for choice in choices:
    # print(choice(choices))
    print(random_choice(choices))
    print(randint(0, choice))


# # Variant 3, import all, DO NOT DO THIS
# from random import *
#
# print(randint(1, 5))


def get_random_index(values):
    return randint(0, len(values) - 1)
