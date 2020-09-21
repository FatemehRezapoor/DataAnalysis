# September 2020
# OBJECCTIVE: Outlier Detection: Use outliers to detect abnormalities such as fraud, cyber security

# Univariate Method: Tukey Boxplots:
# Boxplot whiskers are set at 1.5 * IQR ( Interquartile range : Distance betwee nthe lwoer and upper quartile ). Upper quartile is where the 25% of data are greater than value. Lower quartile is where 25% of data are less than the particular value. Any points beyond 1.5IQR is outlier

# Univariate Method: Tukey outlier labeling
# a= Q1 - 1.5 IQR
# b = Q3 + 1.5 IQR

# it is the manual way of findig box plot


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 5,4
plt.style.use('seaborn-whitegrid')

address = 'D:\Repository\DataScience\iris.data.csv'
df = pd.read_csv(filepath_or_buffer=address, header=None, sep=',')

df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width', 'Species']

# Use data slicing to get specific rows
X = df.iloc[:,0:4].values
y = df.iloc[:,4].values
print(df[:5])

# Identify OUTLIERS from Tukey Boxplots
df.boxplot(return_type='dict')
plt.plot()
plt.show()

# Let's see the outliers by filtering
Sepal_Width = X[:,1]
iris_outliers = (Sepal_Width > 4)
print (df[iris_outliers])
Sepal_Width = X[:,1]
iris_outliers = (Sepal_Width < 2.05)
print (df[iris_outliers])

# Applying Tukey outlier labeling
pd.options.display.float_format = '{:.1f}'.format
X_df = pd.DataFrame(X)
print(X_df.describe())

# So here is what's going on:
# IQR = 3.3 ( Value at 75% ) - 2.8 ( Value at 25% ) = 0.5
# 1.5IQR = 0.75
# 2.8 (value at 25%) - 0.75 = 2.05
# 3.3 (value at 25%) + 0.75 = 4.05
# In this table even minimum value is less than 2.05 so it means there is a high chance it is an outlier.

