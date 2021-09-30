file = open('main.py', 'r')

print(file.readlines())

file = open('d/nested.py', 'r')

print(file.readlines())

file = open('/Users/doncho/repos/softuni-courses/demo-repos/python-advanced-demos/file_handling/main.py')

print(file.readlines())

try:
    file = open('d/random_file_that_does_not_exist_123123ioasdkjvg87fqsad.py', 'r')
    print(file.readlines())
except:
    pass
