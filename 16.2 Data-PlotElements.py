# August 2020
# OBJECCTIVE: DEFINE PLOT ELEMENTS

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

# It is the part of object oriented plotting where you create a figure and then add elements to that figure

# DEFINE AXES, TICKS, GRIDS
rcParams['figure.figsize']=5,4
x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]
fig = plt.figure()
ax=fig.add_axes([.1,.1,1,1])
ax.plot(x,y)
#plt.show()

# set limit to x and y axis
ax.set_xlim([1,9])
ax.set_ylim([0,5])
ax.grid()
ax.plot(x,y)
plt.show()
