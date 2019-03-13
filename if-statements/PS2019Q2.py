import datetime 
#code borrowed from Week2 lecture "thinking like a programmer" snapshot under the title
# 1 is Tuesday, 3 is Thursday
if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3:
    print("Yes - today begins with a T.")
else:
    print("No - today does not begin with a T.")