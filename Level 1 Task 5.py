'''LEVEL 1 TASK 5
PALINDROME CHECK'''

ch=1
while ch==1:
    string=input("Enter string:")
    l=len(string)
    original=string
    string=string.lower()
    j=l-1
    flag=0
    for i in range(0,int(l/2)):
        if string[i]!=string[j]:
            print(original,'is not Palindrome')
            flag=1
            break
        j-=1
    if flag==0:
        print(original,'is Palindrome')
    try:
        ch=int(input("Enter 1 to check more strings:"))
    except:
        break
    print()
