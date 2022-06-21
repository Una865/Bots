#! python3
# pw.py - an insecure password software

PASSWORDS = {
             'email': '74839283Unadj8',
             'blog':'hdjah74yuwdg',
             'uni':'hdbaj6w376dg',
             'github':'test123'
}
import argparse
import pyperclip
ap = argparse.ArgumentParser()
ap.add_argument('acc', action = "store")
args = vars(ap.parse_args())
account = args['acc']

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named '+account)

