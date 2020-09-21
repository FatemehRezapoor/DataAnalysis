# August 2020
# OBJECCTIVE: GROUPING : Used when you want to compare your subsets

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


address = 'D:\Repository\DataScience\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
print(cars.head())
print(cars.shape)

# 1. GROUP THE DATA BY SPECIFIC COLUMN

cars_groups = cars.groupby(cars['cyl'])
# It will group by cylenders
# Now let's get the mean value of the grouped results

print(cars_groups.mean())



