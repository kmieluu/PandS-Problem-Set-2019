i = int(input("Please enter a positive integer: "))

def aga(i): #write a positive integer
    
    a, b = 0, 1
    while a < i:
        print(a, end=' ')
        a, b = b, a+b
    print()
    
# Now call the function we just defined:
aga(2000)

