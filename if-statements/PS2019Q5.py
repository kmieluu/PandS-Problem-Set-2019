# produced basing on week 4 lecture "Continue and break"

for n in range(1000,10000):
    for x in range(1000,n):
       # if number n is dividing by 6 with no decimal places left
       # if number n while dividing by 12 is 
        if n % 6 == 0 and n % 12 == 1:
            print(n)
            break
    else:
        #loop fell through without finding a factor
        next
