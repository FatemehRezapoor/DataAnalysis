# August 2020
# OBJECCTIVE: PLOT FORMATING

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

# It is the part of object oriented plotting where you create a figure and then add elements to that figure


rcParams['figure.figsize']=8,4 # provides the figures size ( width and height in inches)


# LABELLING : FUCNTIONAL METHOD

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]
plt.bar(x,y)
plt.xlabel('your x-axis label')
plt.ylabel('your y-axis label') # Using ylabel function
plt.show()

z = [1,2,3,4,.5]
veh_type = ['bicycle', 'motorbike', 'car', 'van', 'stroller']
plt.pie(z, labels=veh_type)
plt.show()

# LABELLING: OBJECT ORIENTED METHOD

address = 'D:\Repository\DataScience\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = cars.mpg

fig=plt.figure() # Create a fig object
ax = fig.add_axes([.1,.1,1,1]) # Add axes to the figure
ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title('Miles per Gallon of Cars in mtcars Dataset')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')
mpg.plot()
plt.show()

# LAGENDING: FUNCTIONAL METHOD
plt.pie(z)
plt.legend(veh_type, loc='best')
plt.show()

# LEGENDING: OBJECT-ORIENTED METHOD
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title('Miles per Gallon of Cars in mtcars Dataset')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

ax.legend(loc='best')
plt.show()

# ANNOTATING YOUR PLOT
print(mpg.max())
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title('Miles per Gallon of Cars in mtcars Dataset')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

ax.legend(loc='best')

ax.set_ylim([0,45])

ax.annotate('Toyota Corolla', xy= (19,33.9), xytext=(21,35),
           arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
