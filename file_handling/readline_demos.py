print(' --- line by line ---')
file = open('demo.txt', 'r')

while True:
    line = file.readline()
    if not line:
        break
    print(line)

print(' --- line by line with chars count ---')
file = open('demo.txt', 'r')

# while True:
#     line = file.readline(3)
#     if not line:
#         break
#     print(line)

print(file.readline(3))
print(file.readline(3))
print(file.readline(3))

print(' --- all lines ---')
file = open('demo.txt', 'r')
print(file.readlines())
print(file.readlines())

print(' --- line by line with loop ---')
file = open('demo.txt', 'r')
for line in file:
    print(line)

print(' --- line by line with comprehension ---')
file = open('demo.txt', 'r')

print([
    line.strip() for line in file
])
