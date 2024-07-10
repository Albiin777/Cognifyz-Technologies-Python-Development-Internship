'''LEVEL 1 TASK 4
CALCULATOR PROGRAM'''

ch=1
print("CALCULATOR")
while ch==1:
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
    choice=input("Enter operator(+,-,*,/,%):")
    if choice=='+':
        print(a,'+',b,'=',a+b)
    elif choice=='-':
        print(a,'-',b,'=',a-b)
    elif choice=='*':
        print(a,'×',b,'=',a*b)
    elif choice=='/':
        print(a,'÷',b,'=',a/b)
    elif choice=='%':
        print(a,'%',b,'=',a%b)
    else:
        print("INVALID OPERATOR!")
    print()
    try:
        ch=int(input('Enter 1 to continue:'))
    except:
        break
    print()
    
        
        
