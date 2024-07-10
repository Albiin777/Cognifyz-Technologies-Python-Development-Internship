'''LEVEL1 TASK1
STRING REVERSE'''

def reverse_string(string):
    r=-1
    strtlist=list(string)
    print("Reversed String:")
    for i in string:
        print(strtlist[r],end='')
        r-=1
    print('\n')
        
choice=0
while choice==0:
    string=input("Enter String to reverse:")
    reverse_string(string)
    try:
        choice=int(input("Enter 0 to reverse another string..:"))
    except:
        break
    
