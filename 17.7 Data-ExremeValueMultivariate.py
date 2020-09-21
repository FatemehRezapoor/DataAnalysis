# September 2020
# OBJECCTIVE: Outlier Detection: Use multivariate to detect outliers that only show up in the combination of observations from 2 or more different variables.


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

rcParams['figure.figsize'] = 5,4
plt.style.use('seaborn-whitegrid')

address = 'D:\Repository\DataScience\iris.data.csv'
df = pd.read_csv(filepath_or_buffer=address, header=None, sep=',')

df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']

# Use data slicing to get specific rows
X = df.iloc[:,0:4].values
y = df.iloc[:,4].values
print(df[:5])
sb.boxplot(x='Species', y='Sepal Length', data=df, palette='hls')
plt.show()

# Looking at the scatterplot matrix
sb.pairplot(df, hue='Species', palette='hls')
plt.show()
