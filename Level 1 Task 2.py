'''LEVEL1 TASK2
TEMPERATURE CONVERSION'''

ch=1
while ch==1:
    tem=float(input("Enter Temperature:"))
    choice=input("Enter the required scale(C/F:)")
    if choice=='C' or choice=='c':
        cel=0.5555*(tem-32)
        print(tem, "Fahrenheit is", cel,"Celcius")
    elif choice=='F' or choice=='f':
        fahr=1.8*tem+32
        print(tem, "Celcius is", fahr, "Fahrenheit")
    else:
        print("Sorry! Wrong Choice entered")

    print()
    try:
        ch=int(input("Enter 1 to Continue"))
    except:
        break


