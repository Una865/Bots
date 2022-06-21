#!/usr/bin/env python
# if it does not work for you replace '#!/usr/bin/env python' with '#!/usr/bin/env python3'

import sys
import os
import shutil

if len(sys.argv)<2:
    print("use ./indexingFiles.py info")
elif sys.argv[1].lower() =='info':
    print(" ./indexingFiles.py info - get info")
    print(" ./indexingFiles.py <folderPath> - Indexing (renaming) all the files in the folder starting from 0, please enter the full path ")
    print(" ./indexingFiles.py <folderPath> cnt - Indexing (renaming) all the files in the folder starting from cnt, please enter the full path ")
else:

    folder = sys.argv[1]
    if os.path.isdir(folder):
        cnt = 1
        if len(sys.argv) == 3:
            cnt = sys.argv[2]
        for file in os.listdir(folder):

            extension = file.split('.')[-1]
            add = str(cnt)+'.' + extension
            filename = os.path.join(folder,file)
            rename = os.path.join(folder,add)
            print("Renaming {} to {} ...".format(file, add))
            shutil.move(filename, rename)
            cnt += 1
    else:
        print("No such directory as '{}' ".format(folder))


