# August 2020
# OBJECCTIVE: Categorize the data set

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series,DataFrame
import scipy
from scipy import stats

address = 'D:\Repository\DataScience\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
print(cars.carb.value_counts()) # Means there are 10 cars with 4 carb, ...

# Let's make a subset:
cars_cat = cars[['cyl','vs','am','gear','carb']]
print(cars_cat.head())

# LET'S GROUP BY A SPECIFIC VARIABLE: HERE IS GEAR
gear_group=cars_cat.groupby('gear')
print(gear_group.head())
print(gear_group.describe()) # You get 3 rows with 32 columns. There are 3 rows because you only have 3 different gear group. 32 columns becaasue for each column in line 17, the code has generated a description

# 2. TRANSFORM VARIABLES TO CATEGORICAL DATA TYPE
cars['group'] = pd.Series(cars.gear, dtype="category") # Create a new column in the data frame. We are adding a new data to cars and we are diving it a category type.
print(cars['group'].dtype)

# 3. CREATE CROSSTABS
print(pd.crosstab(cars['am'], cars['gear']))
