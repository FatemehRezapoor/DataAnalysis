# August 2020
# OBJECCTIVE: Generating summary statistics using pandas and scipy

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series,DataFrame
import scipy
from scipy import stats

address = 'D:\Repository\DataScience\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
print(cars.head())

# 1. ADDING ALL NUMBERS OF A COLUMN
print(cars.sum()) # Adds value along the columns
print(cars.sum(axis=1)) # Adds values along the rows

# 2. CALCULATE THE MEDIAN and MEAN
print(cars.median())
print(cars.mean())

# 3. CALCUALTE THE MAX VALUE AND FIND THE INDEX
print(cars.max())
print(cars.mpg.idxmax())

# 4. LOOKING AT SUMMARY STATISTICS
print(cars.std()) # Standard deviation of the values
print(cars.var()) # Variance of the values

# 5. FIND UNIQUE VALUES IN THE COLUMN
print(cars.gear.value_counts()) # It says that cars.gear has 15 values with gear 3 and 12 values with gear 4 , ...

# 6. DESCRIBE THE CAR DATA SET
print(cars.describe())