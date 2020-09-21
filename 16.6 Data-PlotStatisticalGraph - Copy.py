# August 2020
# OBJECCTIVE: STATISTICAL GRAPHS

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

# Histograms: Shows a variable distribution as a set of rectangles
# Scatterplot: Shows relationship between variables
# Scatterplot Matrix: Shows the correlations between 2 or more variables
# Boxplot: Good for outlier detection

rcParams['figure.figsize'] = 5, 4
address = 'D:\Repository\DataScience\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars._index = cars.car_names
mpg = cars['mpg']
mpg.plot(kind='hist')
plt.show()

# Another way to plot histograms
plt.hist(mpg)
plt.plot()
plt.show()

# Use seaborn to create the histogram plot
sb.distplot(mpg)
plt.show()

# SCATTER PLOTSS IN ACTION
cars.plot(kind='scatter', x='hp', y='mpg', c=['darkgray'], s=150)
plt.show()
sb.regplot(x='hp', y='mpg', data=cars, scatter=True)
plt.show()

# CREATE SCATTER PLOT MATRIX
# sb.pairplot(cars)
# plt.show() # Takes a long time to process
cars_subset = cars[['mpg', 'disp', 'hp', 'wt']]
sb.pairplot(cars_subset)
plt.show()

# CREATE BOXPLOTS
cars.boxplot(column='mpg', by='am')
cars.boxplot(column='wt', by='am')
sb.boxplot(x='am', y='mpg', data=cars, palette='hls')
plt.show()