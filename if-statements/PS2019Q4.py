# Agata Chmielowiec  
# 16/03/2019
# Program that define if the number is dividable by 2 and divide by 2, if not multiplies by 3 and add 1
# Verbatim from: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

def collatz(num):
    
    if num % 2 == 0:
        result=(num//2)
        print(result)
        return (result)
    elif num % 2 == 1:
        result = num*3+1
        print(result)
        return(result)

n = input("Please enter a positive integer: ")
while n!=1:
    n = collatz(int(n))