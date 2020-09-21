# August 2020
# OBJECCTIVE: PLOT TIMESERIES

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import rcParams

# It is the part of object oriented plotting where you create a figure and then add elements to that figure


rcParams['figure.figsize']=5,4 # provides the figures size ( width and height in inches)


# LABELLING : FUCNTIONAL METHOD
address = 'D:\Repository\DataScience\Superstore-Sales.csv'

df = pd.read_csv(address, index_col='Order Date', encoding='cp1252', parse_dates=True)
print(df.head())
df['Order Quantity'].plot()
plt.show()

# Let's get a small sample of the data
df2 = df.sample(n=100, random_state=25, axis=0) # get the 100 samples from the data with state = 25

plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Superstore Sales')

df2['Order Quantity'].plot()
plt.show()