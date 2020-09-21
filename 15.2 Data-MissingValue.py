# August 2020
# OBJECCTIVE: Treating missing values

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# 1. IDENTIFY MISSING VALUES
series_obj = Series(['row 1', 'row 2', np.nan, 'row 4', 'row 5', 'row 6', np.nan, 'row 8'])
print(series_obj)

# 2. CHECK THE NULL VALUES
print('Null values:',series_obj.isnull())

# 3. FILL IN THE VALUES
np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape(6,6))
print('Data frame is:', DF_obj)
DF_obj.loc[3:5, 0] = np.nan
DF_obj.loc[1:4, 5] = np.nan

# 4. FILL THE NAN WITH 0
filled_DF= DF_obj.fillna(0)
print('Filled frame:\n',filled_DF)

# YOU CAN FILL SPECIFIC VALUES WITH SPECIFIC NUMBERS
filled_DF = DF_obj.fillna({0: 0.1, 5:1.25})
# Fills Nan with index 0 with 0.1

print('Filled frame:\n',filled_DF)

# Fill with the last non Nan value
fill_DF = DF_obj.fillna(method='ffill')
print('Filled frame:\n',fill_DF)

# 5. COUNTING MISSING VALUES
np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape(6,6))
DF_obj.loc[3:5, 0] = np.nan
DF_obj.loc[1:4, 5] = np.nan
print(DF_obj)

# How many missing values per column:
print('Missing values for each column:\n',DF_obj.isnull().sum())

# 6. FILTER MISSING DATA: DROP THE ROWS WITH THE MISSING VALUE
DF_no_NaN = DF_obj.dropna()
print('The only row left with no missing value is:\n',DF_no_NaN)
# DROP THE COLUMNS WITH THE MISSING VALUE
DF_no_NaN = DF_obj.dropna(axis=1)
print('The only column left with no missing value is:\n',DF_no_NaN)
