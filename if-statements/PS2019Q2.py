# Agata Chmielowiec, Navan 2019
# 16/03/2019
# This is a programme that tells if today's day of the week starts with "T" or not
import datetime 
#code borrowed from Week2 lecture "thinking like a programmer" snapshot under the title
# In python numbers of weekday that starts with letter "T" is 1 - Tuesday, 3 - Thursday, all others will have negative result.
if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3:
    print("Yes - today begins with a T.")
else:
    print("No - today does not begin with a T.")