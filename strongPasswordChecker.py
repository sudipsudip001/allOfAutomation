# In this example all we do is try and match characters where the loop exits only if the user
#inputs the correct symbol

import re, sys
def takeNgive(value):
    number = re.compile(r'[0-9]')
    character = re.compile(r'[~!@#$%^&*()_+`\-={}|\[\]\,./<>?:;\'\"]')
    smallLetter = re.compile(r'[a-z]')
    bigLetter = re.compile(r'[A-Z]')
    if(number.search(value) != None):
        if(character.search(value) != None):
            if(smallLetter.search(value) != None):
                if(bigLetter.search(value) != None):
                    if(len(value) >= 8):
                        return 1
    return 0

passer = input()
p = takeNgive(passer)
if(p == 0):
    print('Password is not that safe')
else:
    print('That is a strong password')
