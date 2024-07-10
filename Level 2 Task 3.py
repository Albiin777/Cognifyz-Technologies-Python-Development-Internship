'''LEVEL 2 TASK 3
PASSWORD STRENGTH CHECKER'''

import string
import re

def strengthcheck(password):
    strength=0
    if len(password)>=8:
        strength+=1
    if re.search(r'[a-z]',password):
        strength+=1
    if re.search(r'[A-Z]',password):
        strength+=1
    if re.search(r'[0-9]',password):
        strength+=1
    for i in password:
        if i in string.punctuation:
            strength+=1
            break
    if len(password)<=5:
        strength=2
    if strength==5:
        return("Very Strong!")
    elif strength==4:
        return("Strong!")
    elif strength==3:
        return("Moderate!")
    elif strength==2:
        return("Weak!")
    else:
        return("Very Weak!")
ch=0
while ch==0:
    password=input("Enter Password:")
    print()
    print('Password Strength:',strengthcheck(password))
    try:
        ch=int(input("Enter 0 check another password?:"))
        print()
    except:
        break
