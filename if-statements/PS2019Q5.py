# question about positive integer
a = int(input("Please enter a positive integer: "))

for a in range(1,10):
    for n in range(1,a):
        if a % n == 0:
            print("that is prime")
    
        else: 
            print("that is not prime")