import os

try:
    # Not existing file
    # open('./demo.py')
    # Not existing directory with file
    # open('./nested_dir/demo.txt')
    # A directory, not a file
    # open('./')

    print('File is found')
except FileNotFoundError:
    print('File is not found')
except IsADirectoryError:
    print('File is a directory')
except PermissionError:
    print('No permission to open file')
except FileExistsError:
    print('File already exists for \'x\' mode')


print(os.linesep)  # \n or \n\r
print(os.sep)
