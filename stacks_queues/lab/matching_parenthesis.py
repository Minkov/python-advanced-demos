"""
expression = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
stack = (4,
removed = [9, 21,

closing at 14, opening at 9
    -> expression between 9 and 14
closing at 27, opening at 21
    -> expression between 21 and 27
closing at 28, opening at 4
    -> expression between 4 and 28

# Notes:
- stack has values after expression is complete,
    -> invalid expression
    '1 + (3 + 4'
- At any moment, is closing is found, and stack is empty
    -> invalid expression
    '1 + 3 + 4 )'
"""

# expression = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
expression = input()
parenthesis_indices = []

# for i in range(len(expression)):
#     ch = expression[i]
for index, ch in enumerate(expression):
    if ch == '(':
        parenthesis_indices.append(index)
    elif ch == ')':
        closing_index = index
        opening_index = parenthesis_indices.pop()
        print(expression[opening_index:closing_index + 1])
