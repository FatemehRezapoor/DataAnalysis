# July 2020
# OBJECCTIVE: 1. DATA FRAME IN PANDA: INDEX CSV FILES
import math
import collections
import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

# 1. LOAD FROM A FILE
pd.options.display.max_rows = 16
# We have to provide names to the columns
nobels = pd.read_csv('nobels.csv', names=['year','discipline','nobelist'])
#print(nobels)

# 2. SIMPLE INDEX
print(nobels.index)

# 3. SET YEAR AS INDEX
nobels_by_year = nobels.set_index('year')
print(nobels_by_year)
print(nobels_by_year.index)

# 4. SELECT ALL RECORD FOR THE INDEX
print(nobels_by_year.loc[1901])
# More specific to get series
print(nobels_by_year.loc[1901,'nobelist'])

# 5. SELECT A RANGE
print(nobels_by_year.loc[1914:1918])

# 6. MAKE NEW DATAFRAME WITH NEW INDEX AND SORT
nobels_by_discipline = nobels.set_index('discipline').sort_index()
print(nobels_by_discipline.head())
print(nobels_by_discipline.loc['Medicine':'Peace'])

# 7. MAKE TWO INDEX DATASET IS POSSIBLE TOO
nobels_multi = nobels.set_index(['year','discipline'])
print(nobels_multi)
print(nobels_multi.index)

# Access level 1 & 2
print(nobels_multi.index.get_level_values(0))
print(nobels_multi.index.get_level_values(1))

# SLICING:# to avoid multi-indexing ambiguity, we specify a range of columns (here ":" for all of them)
print(nobels_multi.loc[(slice(1901,1910), 'Chemistry'), :])

# ANOTHER WAY TO ACHIEVE THE SAME RESULTS
print(nobels[(nobels.year >= 1901) & (nobels.year <= 1910) & (nobels.discipline == 'Chemistry')])
# METHOD 2: HOWEVER QUERY MAKES A COMPLETE NEW VAIRABLE SO YOU CANT CHANGE THE ORIGINAL FILE
print('\n',nobels.query('year >= 1901 and year <= 1910 and discipline == "Chemistry"'))