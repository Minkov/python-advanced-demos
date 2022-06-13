from reading import read_until_command

print(
    read_until_command('End')
)

print(
    read_until_command('End', int)
)

print(
    read_until_command('End', lambda x: int(x) + 1)
)

'''
1
2
3
4
5
6
7
End
'''
