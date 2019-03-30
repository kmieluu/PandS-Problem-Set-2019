#Agata Chmielowiec, Navan 2019
#This is a program that sum up positive interegs between 1 and i - the number that user selects.
#Invention taken from 8th February lecture posted: Loops: while and for. 
i = int(input("Please enter a positive integer: "))

total = 0

while i>0:
    total = total + i
    i = i - 1

print(total)
    