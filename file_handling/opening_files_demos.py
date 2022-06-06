import os
from io import open


# import io

def print_contents(file_path):
    print(f' --- Opening {file_path} ---')
    file = open(file_path)
    print(file.read())


# Relative - based on the location of the current file
'''
./ - current directory
    - the directory of the current file
../ - previous directory 
    - the parent directory of the directory of the current file
'''
print_contents('demo.txt')
print_contents('./demo.txt')
print_contents('./opening_files_demos.py')
print_contents('../README.md')
print_contents('../error_handling/custom_exceptions_demos.py')

# Absolute - independent of the location of the current file

print_contents('/Users/doncho/repos/softuni-courses/demo-repos/python-advanced-demos/file_handling/demo.txt')
print_contents(
    '/Users/doncho/repos/softuni-courses/demo-repos/python-advanced-demos/file_handling/opening_files_demos.py')
print_contents('/Users/doncho/repos/softuni-courses/demo-repos/python-advanced-demos/README.md')
print_contents(
    '/Users/doncho/repos/softuni-courses/demo-repos/python-advanced-demos/error_handling/custom_exceptions_demos.py')

# Path separator
'''
Win:
    D:\\repos\\python-advanced
    # D:/repos/python-advanced
Unix/Linux:
    /repos/python-advanced
'''