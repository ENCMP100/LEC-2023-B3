"""
Created on Sun Jan  8 20:06:01 2023

Run the program and review graph in the Plots window in Spyder

@author: ranaweer
"""

from numpy import arange
import matplotlib as plt
"""
    Alternate method: 
        import matplotlib.pyplot as pyplot
"""


x = arange(-10, 11)
y = x ** 2

plt.pyplot.plot(x , y)
plt.pyplot.title('Parabola')
plt.pyplot.xlabel('x')
plt.pyplot.ylabel('y = x ** 2')






