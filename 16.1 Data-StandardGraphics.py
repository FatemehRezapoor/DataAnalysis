# August 2020
# OBJECCTIVE: STANDARD CHART

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

# *** WHAT CHAT TO USE ***
"""
# Line chart: To show changes by time or variables
# Bar chart: To present the categorize data
# Pie chart: To present catagorize data relative to each other
"""
# *** WAYS TO CREATE A PLOT ***
# 1. FUNCTIONAL METHOD: Where you call functions and use them to create the plot
# 2. OBJECT-ORIENTED METHOD: Generate a blank object and fill out with plots

# 1. CREATE A LINE OF CHART FROM A LIST OBJECT

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]
plt.plot(x,y)


# 2. CREATE A LINE OF CHART FROM A PANDAS OBJECT
address = 'D:\Repository\DataScience\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = cars['mpg']
mpg.plot()
plt.show()

# 3. PLOT 3 VARIABLES IN A CHART
df = cars[['cyl','wt','mpg']]
df.plot()
plt.show()

# 3. CREATE A BAR CHART FROM A LIST OBJECT
plt.bar(x,y)

# 4. CREATE A BAR CHART FROM A PANDAS OBJECT
mpg.plot(kind="bar")
plt.show()
# To make the chart horizentally:
mpg.plot(kind="barh")
plt.show()

# 5. TO MAKE A PIE CHART
x = [1,2,3,4,0.5]
plt.pie(x)
plt.show()
# Save the figure
plt.pie(x)
plt.savefig("My Pie.png")
plt.show()


