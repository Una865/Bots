#!/usr/bin/env python
#bulletPointAdder.py - adding bullets to wiki markup

import pyperclip
text = pyperclip.paste()
listText = text.split('\n')
for i in range(len(listText)):
    listText[i] = '* '+listText[i].lstrip()
text = '\n'.join(listText)
pyperclip.copy(text)

print(listText)
