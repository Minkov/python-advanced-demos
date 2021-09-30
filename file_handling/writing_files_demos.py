def write_to_file(file_path, mode, text):
    # file = open(file_path, mode)
    # file.write(text)
    # file.close()
    with open(file_path, mode) as file:
        file.write(text)


write_to_file('files/numbers.txt', 'a', '''1''')

x = 5
write_to_file('files/numbers.txt', 'a', '''NEW
TEXT
''')
y = 7


def write(file, text):
    file.write(text)


def open_file(file_path):
    return open(file_path, 'a')


def close_file(file):
    file.close()


file = open_file('files/new-file.txt')
write(file, 'asd')
write(file, 'asd')
write(file, 'asd')
write(file, 'asd')
write(file, 'asd')
close_file(file)
