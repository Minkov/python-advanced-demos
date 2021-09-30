import os
from os import path

# open('sample-a.txt', 'w')
# confirm = input('Are you sure ....?')
# if confirm == 'y':
# if path.exists('sample-a.txt'):
#     os.remove('sample-a.txt')
#
# [print(x) for x in os.listdir('.')]
# print('-----')
# [print(x) for x in os.listdir('lab')]

ss = [os.getcwd()]

while ss:
    current_dir = ss.pop()
    print(current_dir)
    if path.isfile(current_dir):
        continue

    for file_path in os.listdir(current_dir):
        absolute_path = path.join(
            current_dir,
            file_path
        )
        ss.append(absolute_path)

#
# for file_name in os.listdir():
#     full_path = path.join(
#         os.getcwd(),
#         file_name
#     )
#     print(full_path)
