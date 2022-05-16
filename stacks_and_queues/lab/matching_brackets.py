'''
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
s = [

'1' not a bracket
...
'(' is opening bracket
    -> add its index to the stack
'2' not a bracket
...
'(' is opening bracket
    -> add its index to the stack
'2' not a bracket
...
')' is closing bracket
    -> pop the top from the stack
    -> subexpression is between top of stack and this closing bracket
    -> 9, 15 => (2 + 3)
' ' not a bracket
...
'(' is opening bracket
    -> add its index to the stack
'3' not a bracket
...
')' is closing bracket
    -> pop the top from the stack
    -> subexpression is between top of stack and this closing bracket
    -> 23, 29 => (3 + 1)
')' is closing bracket
    -> pop the top from the stack
    -> subexpression is between top of stack and this closing bracket
    -> 4, 30 => (2 - (2 + 3) * 4 / (3 + 1))
'''

# expression = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
# expression = '(2 + 3) - (2 + 3)'
expression = input()

s = []
for i in range(len(expression)):
    ch = expression[i]
    if ch == '(':
        s.append(i)
    elif ch == ')':
        start_index = s.pop()
        end_index = i + 1
        print(expression[start_index:end_index])

count = 0
for ch in expression:
    if ch == '(':
        count += 1
    elif ch == ')':
        count -= 1

'''
# Variants
Is expression valid?
    - stack should be empty at the end
    - Better to do the following:
        - when '(' +1
        - when ')' -1
        - 0 at the end

(((1123 + 23) => count = 2 - invalid
(123 + 123))) => count < 0 - invalid
)()( => count = 0, but invalid 
'''
