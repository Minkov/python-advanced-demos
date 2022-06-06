from os import remove
from os.path import exists

file_path = './files/to_delete.txt'

# open(file_path, 'w').close()
if exists(file_path):
    remove(file_path)
    print('File deleted')
else:
    print('File already deleted')
