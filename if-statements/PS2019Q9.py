#Agata Chmielowiec, Navan 2019
#Program that will open the text file and read every second line
# Python module SYS presented in lecture: https://web.microsoftstream.com/video/65df155a-ac29-460b-869d-2de6ffc6c3fc
# Lecture 7 & 6 
# Verbatim: https://stackoverflow.com/a/30551984

import sys

if len(sys.argv) == 1: # the number of object to be entered on the command line in order to open the textfile is set to one, i.e. Solution-9 

    print ("Opening Belmullet.txt now")

    with open("Belmullet.txt", "r") as f:
        
            for count, line in enumerate(f, start=0):  
                if count % 2 != 0:      # if the line is uneven   
                    print(line)         # print the line
