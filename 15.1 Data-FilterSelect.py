# August 2020
# OBJECCTIVE: DATA PREPERATION: REMOVE DUPLICATES

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

""" SERIES:"""

# 1. MAKE SERIES
series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6','row 7', 'row 8'])
print(series_obj)

# 2.INDEX SERIES. You can write an index value in two forms.
# - Label index or
# - Integer index

# Access the index
print('Label index:', series_obj['row 7'],'\n','Integer index:',series_obj[[0,7]])

# 3. DATA SLICING:You can use slicing to select and return a slice of several values from a data set. Slicing uses index values so you can use the same square brackets when doing data slicing.

print('Series slicing by index:\n',series_obj[0:3],'\n','Series slicing by label:\n',series_obj['row 0':'row 3'] )

# 4. SET THE SERIES VALUES
series_obj['row 0'] = 8
print('This is the new value:', series_obj['row 0'])

""" DATA FRAME:"""

# 1. Let's create a data frame
np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)), index=['row 1', 'row 2', 'row 3', 'row 4','row 5','row 6'], columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
print('Frame is \n: ',DF_obj)

# 2. Access the index
print('Index is \n: ',DF_obj.loc[['row 2', 'row 5'], ['column 5', 'column 2']])

# 3. DATA SLICING:You can use slicing to select and return a slice of several values from a data set. Slicing uses index values so you can use the same square brackets when doing data slicing.


# 4. BOOLEAN MASKING
print('Boolean mask:\n',DF_obj<0.2)
print('Data Frame with condition is:\n',DF_obj[DF_obj>0.2])


