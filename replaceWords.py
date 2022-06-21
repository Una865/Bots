import argparse
import os
import re

ap = argparse.ArgumentParser()
ap.add_argument('path', action = 'store', help = 'Path to a text file to read from')
args = vars(ap.parse_args())

if os.path.isfile(args['path']):

    file = open(args['path'])
    newFile = open('results.txt','w')
    wordReg = re.compile(r'ADJECTIVE|NOUN|VERB')
    text = file.read()
    print(text)
    for i in wordReg.findall(text):
        inp = input('Enter the substitution for %s:' % i)
        reg = re.compile(r'{}'.format(i))
        text = reg.sub(inp,text,1)
    newFile.write(text)
    print('All the words replaced.')

else:
    print('No such file or directory')










