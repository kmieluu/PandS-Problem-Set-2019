#Agata Chmielowiec, Navan 2019
#Problem no. 8: A code that will say what date is today in format "Monday, January 10th 2019 at 1:15pm"
#Verbatim: https://docs.python.org/3/tutorial/stdlib.html#dates-and-times


from datetime import datetime 
now = datetime.today()
day = now.strftime("%d")
h = now.strftime("%H")

if day == (1,21,31):
    end = 'st'

if day ==(2,22):
    end = 'nd'

if day ==(3,23):
    end = 'rd'

else:
    end = 'th'

if h < '12:00':
    h = 'am'

else:
    h = 'pm'

print(now.strftime(f"%A, %B %d{end} %Y at %H:%M{h}"))
