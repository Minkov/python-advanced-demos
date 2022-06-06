file_path = './demo.t2xt'

file1 = open(file_path, 'w')
file2 = open(file_path, 'w')

file1.write('file 1')
file1.close()
file1.write('file 11')
file2.write('file 2')
