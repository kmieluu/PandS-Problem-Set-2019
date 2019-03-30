#Agata Chmielowiec, Navan March 2019
# Task 7 from the Problem Set 2019 list
#Programme that takes a positive floating point number as input and outputs an approximation of its square root

#Reference to lecture from week 8 - Project and problem set, lecture: Newton's square root

#The number to calculate square root of
rootof = 100

#The initial estimate for the square root
estimate = 8

#Keep going untill square of estimate is within 0.1 of rootof
while abs ( (estimate * estimate )- rootof) > 0.1:
    #This is Newton's method to improve our estimate
    #Adapted from lecture

    estimate -= ((estimate * estimate )-rootof) / (2 * estimate)

#print the result
print(f"The square root of {rootof} is approx. {estimate}.")