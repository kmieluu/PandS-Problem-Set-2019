    # produced basing on week 4 lecture "Continue and break"

for n in range(1000,10000):
    for x in range(1000,n):
       # numbers that are divisible by 6 (there will be 2x more) but not 12
       # if number n is divisible by 6 with no decimal places left (decimal place = 0)
       # AND
       # from number that is divisible by 6 check if divisible by 12 and 
       # throw away all that are 
        if n % 6 == 0 and n % 12 != 0:
            print(n)
            break
    else:
        #loop fell through without finding a factor
        next
