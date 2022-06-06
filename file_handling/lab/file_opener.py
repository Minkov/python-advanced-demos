file_path = './text.txt' # File found
# file_path = './text2.txt'  # File not found

try:
    open(file_path, 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')
