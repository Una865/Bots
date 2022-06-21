#!/usr/bin/env python

import zipfile
import os


def zipper(folder, extension,name):



    folder = os.path.abspath(folder)
    zipf =  name + '.zip'
    newZip = zipfile.ZipFile(zipf,'w')
    for foldername, subfolder, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                path = os.path.join(foldername,filename)
                newZip.write(path, os.path.basename(path))
                #newZip.write(filename)

    newZip.close()

import sys
if len(sys.argv) < 2:
    print("See info by running -> ./zipper.py info")
elif sys.argv[1].lower() == 'info':
    print("./zipper.py <folder_path> <extension> <zip file name>  - zip all files in the current folder with the specified extension")
else:

    folder = sys.argv[1]
    extension = sys.argv[2]
    zipf = sys.argv[3]

    zipper(folder,extension,zipf)

    print("Done")



