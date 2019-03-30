#Agata Chmielowiec, Navan 2019
#Problem no. 8: A code that will say what date is today in format "Monday, January 10th 2019 at 1:15pm"
#Verbatim: https://docs.python.org/3/tutorial/stdlib.html#dates-and-times


#time = time.asctime([time])
# dates are easily constructed and formatted

from datetime import datetime
now = datetime.today()
day = now.strftime("%d")


print(now.strftime(f"%A, %B %d %Y at %H:%Mpm"))

# dates support calendar arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday