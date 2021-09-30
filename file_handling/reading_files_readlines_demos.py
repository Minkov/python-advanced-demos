file = open('reading_files_readlines_demos.py', 'r')
x = 5


# print(file.readlines())

def read_nth_line(file_path, n):
    file = open(file_path, 'r')
    for i in range(n - 1):
        file.readline()
    return file.readline()


nth_line = 5
result = read_nth_line('reading_files_readlines_demos.py', nth_line)

print(result)
i = 1
# # for line in file.readlines():
# #     print(f'{i}: {line}')
# #     i += 1
#

# generators
for line in file:
    print(f'{i}: {line}')
    i += 1

#  docx, xlsx
