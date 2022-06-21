import re
import pyperclip

text = str(pyperclip.paste())
phoneNumRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?   # optional area code
(\s|-|\.)?  # optional separator
(\d{3})    # first three digits
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''',re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''',re.VERBOSE)
matches = []
for groups in phoneNumRegex.findall(text):
    phoneNum = '-'.join(groups[1],groups[3],groups[5])
    if groups[8]!='':
        phoneNum+= ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to the clipboard:")
    print('\n'.join(matches))
else:
    print("No phone numbers or e-mail addresses found.")
    



