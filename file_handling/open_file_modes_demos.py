# open('./demo.txt')
# # Same as:
# open('./demo.txt', 'r')
# # Same as:
# open('./demo.txt', 'rt')

print(open('./demo.txt', 'rt').read())
print('-' * 20)
print(open('./demo.txt', 'rb').read())

print('-' * 20)
print('-' * 20)
print('-' * 20)

# print(open('./demo.png', 'rt').read())
print('-' * 20)
print(open('./demo.png', 'rb').read())
