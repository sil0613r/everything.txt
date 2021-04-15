import shutil
import sys
import random

file_name = random.randint(0, 3)

if file_name == 0:
    file_name = 'why'
elif file_name == 1:
    file_name = 'gl reading that'
elif file_name == 2:
    file_name = '😭'
elif file_name == 3:
    file_name = 'dont'

file_path = sys.argv[1] if len(sys.argv) > 1 else print('too many arguments')
shutil.copy2(file_path, '%s.txt' % file_name)
