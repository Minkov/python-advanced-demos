import sys
from io import StringIO

from lab.fibonacci_sequence import create_sequence, locate
from reading import read_until_command

test_input = '''Create Sequence 10
Locate 13
Create Sequence 3
Locate 10
Stop
'''


def parse_command(command):
    parts = command.split(' ')
    if parts[0] == 'Create':
        return ('Create', int(parts[2]))
    else:
        return ('Locate', int(parts[1]))


sys.stdin = StringIO(test_input)
commands = read_until_command('Stop', map_func=parse_command)

for (command, value) in commands:
    result = None
    if command == 'Create':
        result = create_sequence(value)
    elif command == 'Locate':
        result = locate(value)

    print(result)
