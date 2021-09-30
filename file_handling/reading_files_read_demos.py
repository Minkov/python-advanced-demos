x = 5
file = open('reading_files_read_demos.py', 'r')

# print(file.read()) # Reads all


while True:
    text = file.read(22)
    print(text)
    print('--------')
    if not text:
        break

'''
7GB = 7*1000MB=7*1000*1000KB=7*1000*1000*1000B
7GB text file => RAM

10000B ~= 10KB
'''
