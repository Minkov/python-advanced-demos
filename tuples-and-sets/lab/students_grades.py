import sys
from io import StringIO
from statistics import mean
from time import time

test_input1 = '''7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.00
'''

test_input2 = '''4
Scott 4.50
Ted 3.00
Scott 5.00
Ted 3.66
'''

test_input3 = '''5
Lee 6.00
Lee 5.50
Lee 6.00
Peter 4.40
Kenny 3.30
'''

sys.stdin = StringIO(test_input1)


def avg(values):
    return sum(values) / len(values)


n = int(input())

students_records = {}

for _ in range(n):
    name, grade_string = input().split(' ')
    grade = float(grade_string)

    if name not in students_records:
        students_records[name] = []
    students_records[name].append(grade)

for name, grades in students_records.items():
    average_grade = avg(grades)
    grades_str = ' '.join(str(f'{x:.2f}') for x in grades)
    print(f'{name} -> {grades_str} (avg: {average_grade:.2f})')

# Break to 19:40


x = 12.146001
print(x)
print(f'{x:.3f}')
