#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\+\d{3}|d{3})?          # Country extension which is optional
    (\s|-)?             # separator which is also optional
    (\d{2})     # first two digits in case they are separated as district codes
    (-)?          # the case where the hyphen separates part of the phone number
    (\d)
    (-)?
    (\d)
    (-)?
    (\d{6})
    )''', re.VERBOSE)

#TODO: Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+          # Username
    @                  # @ symbol
    [a-zA-Z0-9.-]+               # domain name
    (\.[a-zA-Z]{2,7})        # dot-something
    )''', re.VERBOSE)

#TODO: Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    matches.append(groups[0])
for groups in emailRegex.findall(text):
    matches.append(groups[0])


#TODO: Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
