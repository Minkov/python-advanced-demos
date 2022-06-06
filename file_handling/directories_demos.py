from os import mkdir, rmdir, listdir
from os.path import join, abspath

directory_path = './'
# mkdir('./dir_to_delete')
# time.sleep(10)
# rmdir('./dir_to_delete')

files_and_dirs_names = listdir(directory_path)
files_and_dirs = [
   abspath(join(directory_path, f)) for f in files_and_dirs_names
]

[print(f) for f in files_and_dirs_names]
[print(f) for f in files_and_dirs]
