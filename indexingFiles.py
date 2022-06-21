#!/usr/bin/env python

import sys
import os
import shutil

if len(sys.argv)<2:
    print("use ./indexingFiles.py info")
elif sys.argv[1].lower()=='info':
    print(" ./indexingFiles.py info - get info")
    print(" ./indexingFiles.py <folderName> - Index (renaming) all the files in the folder starting from 1, please enter the full path ")
else:

    folder = sys.argv[1]
    if os.path.isdir(folder):
        cnt = 0
        for file in os.listdir(folder):
            cnt += 1
            extension = file.split('.')[-1]
            add = str(cnt)+'.' + extension
            filename = os.path.join(folder,file)
            rename = os.path.join(folder,add)
            print(rename)
            shutil.move(filename,rename)
    else:
        print("No such directory as '{}' ".format(folder))


