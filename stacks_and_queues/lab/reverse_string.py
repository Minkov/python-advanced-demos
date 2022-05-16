# Better solutions
# original_string[::-1]
# original_string.reverse()

# original_string = 'I love python'
# original_string = 'Stacks and Queues'

original_string = input()

s = []
for c in original_string:
    s.append(c)  # push into the stack

reversed_string = ''

while s:
    value = s[-1]  # peek
    reversed_string += value
    s.pop()  # pop the top

print(reversed_string)
