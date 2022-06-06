file_path = './demo.txt'

print(' --- Whole file ---')
file = open(file_path, 'r')
print(file.read())

print(' --- by bytes count')
file = open(file_path, 'r')
while True:
    chars = file.read(3)
    if not chars:
        break
    print(chars)
