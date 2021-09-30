file_name = 'text.txt'

try:
    open(file_name, 'r')
    print('File found')
except:
    print('File not found')
