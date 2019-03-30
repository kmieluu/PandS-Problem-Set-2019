#Agata Chmielowiec, Navan 2019
#Basing on Continue & Break lecture I managed to write easier query to get the same result.

n = int(input("Please enter a positive integer: "))

for x in range (2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n//x)
            break
else:
        print(n, "value selected. Please input a positive integer value.")