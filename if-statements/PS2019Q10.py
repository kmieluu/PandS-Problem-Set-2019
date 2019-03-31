# Agata Chmielowiec, Navan 2019
# Write a function that displays in range [0,4] functions x, x^2 and 2^x
# reference: https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
# reference2: https://matplotlib.org/tutorials/introductory/pyplot.html

import matplotlib.pyplot as pl
import numpy as np

#Define x axis: from 0 moved by 5 so 0,1,2,3,4 within 1 as separator. As per task plot should display plot [0,4]
x = np.arange(0.00, 5.00, 1.00)

#Define the function's as per task requiremens
y1 = x
y2 = x**2
y3 = 2**x

# present the y functions
pl.plot(x, y1, 'g') # green line
pl.plot(x, y2, 'r') # red line
pl.plot(x, y3, 'yo') # yellowo dots

#Labelling graph verbatim: https://matplotlib.org/gallery/subplots_axes_and_figures/axes_demo.html 
pl.xlabel('X')
pl.ylabel('Y')
pl.title('X, X^2,2^X functions - Question 10 Solution')

#Legend details
pl.legend(['y1 = x', 'y2 = x^2', 'y3 = 2^x'])

#Show grid lines
pl.grid(axis='both')

#display graph
pl.show()