# August 2020
# OBJECCTIVE: Treating missing values

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

DF_obj= DataFrame({'column 1':[1,1,2,2,3,3,3],'column 2':['a', 'a','b', 'b', 'c', 'c', 'c'],'column 3':['A', 'A', 'B', 'B', 'C', 'C', 'C']})
print(DF_obj)

# 1. REMOVE DUPLICATES WITHIN THE ROW:
# Check each row and compare to the previouse rows to see if it is the duplicate of another row in the data frame

row_duplicate = DF_obj.duplicated()
print(row_duplicate)

# 2. IDENTIFY AND DROP THE THE DUPLICATES. CREATE A NEW DATA FRAME WITH NO DUPLICATES

DF_obj_drop=DF_obj.drop_duplicates()
print('Row Duplicate:\n',DF_obj_drop)


# 3. REMOVE DUPLICATES WITHIN THE COLUMNS:

DF_obj= DataFrame({'column 1':[1,1,2,2,3,3,3],'column 2':['a', 'a','b', 'b', 'c', 'c', 'c'],'column 3':['A', 'A', 'B', 'B', 'C', 'D', 'C']})

print(DF_obj)
column_duplicate= DF_obj.duplicated(['column 3'])
print(column_duplicate)

# 4. DROP THE DUPLICATES. CREATE NEW DATA FRAME WITH NO DUPLICATES
DF_obj_drop= DF_obj.drop_duplicates(['column 3'])
print('Column Duplicate:',DF_obj_drop)



