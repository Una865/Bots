#!/usr/bin/env python
import shelve
import pyperclip
import sys


'''
Usage:  ./mycpb.py save <keyword> - saves clipboard 
        ./mycpb.py <keyword>  - saves information from file to clipboard
        ./mycpb.py list - loads everything you have copied 
        ./mycpb.py show - shows everything you have copied 
        ./mycpb.py info
'''


myclipBShelf = shelve.open('mycpb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    print("************************************************************************")
    myclipBShelf[sys.argv[2]] = pyperclip.paste()
    print("The content of clipboard saved under the keyword:", sys.argv[2])
    print("************************************************************************")

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'info':
        print("************************************************************************")
        print("Usage constructions:")
        print("./mycpb.py save <keyword> - saves clipboard ")
        print("./mycpb.py <keyword>  - saves information from file to clipboard")
        print("./mycpb.py list - loads everything you have copied ")
        print("./mycpb.py show - shows everything you have copied ")
        print("************************************************************************")

    elif sys.argv[1].lower() == 'list':
        print("************************************************************************")
        print("Everything saved in the script is copied to the clipboard")
        pyperclip.copy(str(list(myclipBShelf.keys())))
        print("************************************************************************")
    elif sys.argv[1].lower() == 'show':
        print("************************************************************************")
        print("Content that you saved:")
        for key in myclipBShelf.keys():
            print(key,"->",myclipBShelf[key])
        print("************************************************************************")

    elif sys.argv[1] in myclipBShelf:
        print("************************************************************************")
        print("Content under the keyword:",sys.argv[1],"copied to the clipboard")
        pyperclip.copy(myclipBShelf[sys.argv[1]])
        print("************************************************************************")




myclipBShelf.close()
