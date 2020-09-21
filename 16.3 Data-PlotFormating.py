# August 2020
# OBJECCTIVE: PLOT FORMATING

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

# It is the part of object oriented plotting where you create a figure and then add elements to that figure


rcParams['figure.figsize']=5,4 # provides the figures size ( width and height in inches)
x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]
plt.bar(x,y)
plt.show()

# DEFINE PLOT COLOR
plt.figure
wide= [.5,.5,.5,.9,.9,.9,.5,.5,.5] # Change the width of the bar
color = ['salmon']
plt.bar(x, y, width=wide, color=color, align='center')
plt.show()

# READ THE CSV AND PLOT FROM DATAFRAME
address = 'D:\Repository\DataScience\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = cars[['cyl','mpg','wt']]
mpg.plot()
plt.show()

# Let's change the colors
color_theme = ['darkgray', 'lightsalmon', 'powderblue']
mpg.plot(color=color_theme)
plt.show()

# Change the color based on RGB code
z = [1,2,3,4,.5]
plt.pie(z)
plt.show()

color_theme = ['#A9A9A9', '#FFA07A', '#B0E0E6', '#FFE4C4', '#BDB76B']
plt.pie(z, colors=color_theme)
plt.show()

# CHANGE THE LINE STYLE
x1 = range(0,10)
y1 = [10,9,8,7,6,5,4,3,2,1]

plt.plot(x, y)
plt.plot(x1, y1)
plt.show()
plt.plot(x, y, ds='steps', lw=5)
plt.plot(x1, y1, ls='--', lw=10)
plt.plot(x, y, marker='1', mew=20)
plt.plot(x1, y1, marker='+', mew=15)
plt.show()