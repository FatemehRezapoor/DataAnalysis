# July 2020
# OBJECCTIVE: 1. DATA FRAME IN PANDA/ READ FROM CSV FILES
import math
import collections
import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

# 1. LOAD FROM A FILE
pd.options.display.max_rows = 16
nobel=pd.read_csv('nobels.csv')
print(nobel)
# We have to provide names to the columns
nobels = pd.read_csv('nobels.csv', names=['year','discipline','nobelist'])
print(nobels)

# 2. LET'S GET THE FILE INFORMATION
print(nobels.info())

# 3. PRINT HEAD: THE FIRST FEW AND LAST FEW ROWS
print(nobels.head())
print(nobels.tail())

# 4. PRINT COLUMNS + DTYPE + INDEX
print(nobels.columns)
print(nobels.dtypes)
print(nobels.index)
print(nobels['year']) # Result is a series
print(nobels.discipline.values[:50])

# 5. GET UNIQUE VALUES
print(nobels.discipline.unique())
# 6. COUNT TIMES EACH ITEM APPEARS
print(nobels.nobelist.value_counts())

# 7. SELECT JUST PHYSICS
print(nobels[nobels.discipline == 'Physics'])


# 8. SELECT AS A QUERY INTERFACE
print(nobels.query('discipline == "Chemistry"'))

# 9. LOOK FOR AND SELECT A SPECIAL PERSON
print(nobels[nobels.nobelist.str.contains('Curie')])

# 10. READ FROM NUMPY FILE
disco = np.load('discography.npy')
print(disco)
# 11. CREATE A DATA FRAME
disco_df = pd.DataFrame(disco)
print(disco_df)





