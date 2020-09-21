# August 2020
# OBJECCTIVE: CONCATENATION + TRANSFORMATION

# CONCATENATE: Combine data from different sources
# TRANSFORMATION: Modify data in to different formats

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
print(DF_obj)

DF_obj_2 = pd.DataFrame(np.arange(15).reshape(5,3))

print(DF_obj_2)

# 1. CONCATENATING DATA

# Along the row
DF_obj_row=pd.concat([DF_obj, DF_obj_2], axis=0)
print('Concat on row:\n',DF_obj_row)

# Along the column
DF_obj_col=pd.concat([DF_obj, DF_obj_2], axis=1)
print('Concat on column:\n',DF_obj_col)

# 2. TRANSFORMING DATA
# 2.1 DROP DATA

# Along the row : Drops row= 0 and 2

DF_obj_drop=DF_obj.drop([0,2])
print('Drop row\n',DF_obj_drop)

# Along the column:

DF_obj_drop=DF_obj.drop([0, 2], axis=1)
print('Drop column\n',DF_obj_drop)

# 3. ADDING DATA
series_obj = Series(np.arange(6))
series_obj.name = "added_variable"
print(series_obj)

# 3.1 JOIN SERIES TO DATA FRAME
"""
LEARN: There are multiple ways to combine dataframes:

Merge: Works when the data frames have the same index. If the index is different you will get an error. So if you want to add data frames with similar index go with the merge.

"""
variable_added = DataFrame.join(DF_obj, series_obj)
print('Join\n',variable_added)


# 3.2 APPEND DATA
added_datatable = variable_added.append(variable_added, ignore_index=False) # index is set to false, so it will not start a new indexing. If set to True, it will start a new index
print('Append index False:\n',added_datatable)

added_datatable = variable_added.append(variable_added, ignore_index=True)
print('Append index True:\n',added_datatable)

# Some examples:
s= DF_obj.append(series_obj, ignore_index=True)
print('Append series:\n',s)
s= DF_obj.append(DF_obj_2, ignore_index=False)
print('Append series:\n',s)
s= pd.concat([DF_obj,series_obj],axis=1)
print('Concat:\n',s)

# 4. SORT DATA
# Sort by the values along either axis.
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
print(df)
print('Sorted based on col1:\n', df.sort_values(by=['col1']))
# Sorts based on the column 1. It will re-arrange other rows based on the column 1 two.

# To sort based on 1 and then 2 column
print('Sorted based on col 1, 2 \n', df.sort_values(by=['col1', 'col2'])
)





