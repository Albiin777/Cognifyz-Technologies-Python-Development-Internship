'''LEVEL 2 TASK 4
FIBONACCI SEQUENCE'''

def Fibonacci(number):
    prev=0
    current=1
    print("Fibonacci Sequence:")
    for i in range(0,n):
        print(prev,end=' ')
        nextt=current+prev
        prev=current
        current=nextt        
ch=0
while ch==0:
    try:
        n=int(input('Enter no. of terms:'))
    except:
        print("Enter integer value!")
    Fibonacci(n)
    try:
        ch=int(input("\nEnter 0 to generate another:"))
        print()
    except:
        break
