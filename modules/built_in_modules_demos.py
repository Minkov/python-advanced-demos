import sys

from collections import deque
from io import StringIO
from os import path
import random

print(path.join('parent', 'child'))


test_input1 = '''1
2
3
'''

sys.stdin = StringIO(test_input1)
fake_stdout = StringIO('')

x = int(input())
y = int(input())
z = int(input())

print(x + y + z)

q = deque()

ll = ['One', 'Two', 'Three', 'Four', 'Five']

print(random.randint(1, 10))
print(random.choice(ll))
