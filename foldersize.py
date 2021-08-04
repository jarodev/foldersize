import os
import pandas as pd
import sys
import humanize as hu

if len(sys.argv) < 2:
    start_path = "."
else:
    start_path = sys.argv[1]

size_list = []
total_size = 0

for dirpath, dirnames, filenames in os.walk(start_path):

    path_size = 0
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if not os.path.islink(fp):
            total_size += os.path.getsize(fp)
            path_size += os.path.getsize(fp)

    size_list.append({"name": dirpath, "size": hu.naturalsize(path_size, binary= True)})
    print(dirpath, ":", hu.naturalsize(path_size, binary= True))

pd.DataFrame(size_list).to_excel('output.xlsx')

print('Folder size:', hu.naturalsize(total_size, binary=True))
