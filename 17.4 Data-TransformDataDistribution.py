# September 2020
# OBJECCTIVE: Transforming dataset distributions: Scale your data
# Normalize the data: putting each observation on the relative scale
# Use scikit learn to: Scale, Center, Normalize , Bin and impute data

import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')


address = 'D:\Repository\DataScience\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# Let's isolate a variable
mpg = cars.mpg
plt.plot(mpg)
plt.show()
print(cars[['mpg']].describe())

# Let's make a matrix
mpg_matrix = mpg.values.reshape(-1,1)
# Scale the values from 0 to 1
scaled = preprocessing.MinMaxScaler()
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)
plt.show()

# Scale at different range
scaled = preprocessing.MinMaxScaler(feature_range=(0,10))
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)
plt.show()

# Use scale to scale your features
# let's create a variable with no min and standard deviation value
standardized_mpg = scale(mpg, axis=0, with_mean=False, with_std=False)
plt.plot(standardized_mpg)
plt.show()

# Use default values
standardized_mpg = scale(mpg)
plt.plot(standardized_mpg)