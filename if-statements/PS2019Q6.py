#Agata Chmielowiec, Navan 2019
#This programme shows every second word of the sentences imported.
# User inputs the string
i = (input("Write your sentence here: "))
#at the moment the output we want to see is blank
str_out = ''
#because the word we want to see first will be the first inputted by used word count = 1
count = 1 

#for LOOP: for whole sentence inputted we search for spaces that separate words.
#we want the code to run whole sentence so no breaks

for a in i:

    if a == ' ': #after first word is over (for python is word number 0)
        count = count + 1 #our count changes from what it was to +1
        if count % 2 == 0: # then if new count modulus 2 = 0
            str_out = str_out + ' ' #output will be nothing (from the beginning) + space
    elif count % 2 == 1: #however if number of space + 1 modulus 2 does not equal 0
            str_out = str_out + a # then print nothing(from beginning) + whatever word in i is between last space and next space
print(str_out) #print it