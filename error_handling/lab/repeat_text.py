import sys
from io import StringIO

test_input1 = '''Hello
Bye
'''

test_input2 = '''Hello
2
'''

# sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)

text = input()

try:
    times = int(input())
    print(text * times)
except ValueError:
    print('Variable times must be an integer')
