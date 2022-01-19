import os
import stat


access = {
    0: "---",
    1: "--x",
    2: '-w-',
    3: '-wx',
    4: 'r--',
    5: 'r-x',
    6: 'rw-',
    7: 'rwx'
  }

oct_folder_access = oct(stat.S_IMODE(os.lstat(".").st_mode))

for value in oct_folder_access[-3:]:
    print(access[int(value)], end='')
