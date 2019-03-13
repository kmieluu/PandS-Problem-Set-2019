

i = int(input("Please enter a positive integer: "))

parzyste = i/2
nieparzyste = i*3+1
for i in range(1,i):
    if i % 2 == 0:
        i=i/2
        print(i)         
    elif i % 2 != 0:
        i=i*3+1

print(i)      
        