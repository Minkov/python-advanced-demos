#      0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15
tt = ('1', '2', '3', '2', '4', '5', '1', '2', '3', '4', '5', '3', '3', '6', '7', '8')
'''
1 -> 2
2 -> 3
3 -> 4
'''

print(tt)
print(' --- count ---')
print(tt.count(1))
print(tt.count(2))
print(tt.count(3))

print(' --- index ---')
print(tt.index('1'))  # equivalent to tt.index(1, 0)
print(tt.index('1', 1))
# print(tt.index(1, 7)) # raises exception

print(' --- in ---')
print('1' in tt)
print('17' in tt)

print(' --- loops ---')
for value in tt:
    print(value)

print(' --- list comprehensions ---')
[print(x) for x in tt]

print(' --- other objects ---')
print(f'str.join(): {", ".join(tt)}')
print(f'len(): {len(tt)}')

print(' --- tuple concatenation ---')
print((1, 2) + (3, 4, 5))
