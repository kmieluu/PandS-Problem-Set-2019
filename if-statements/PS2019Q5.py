# Agata Chmielowiec, Navan 2019
# 
# 
# This is a programme that tell you if selected positive integer is a prime number or not.
# Prime number is positive number that divides by 1 and itself only.
a = int(input("Please enter a positive integer: "))

if a > 0: 
    for i in range(2,a):

        if(a % i) == 0:
            print(a, "is not a prime number.")
            break
    else:
        print(a, "is a prime number.")

else:
    print(a, "value selected. Please input a positive integer value.")