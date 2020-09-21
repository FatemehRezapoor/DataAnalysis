# August 2020
# OBJECCTIVE: Parametric Corrolation: Find the relation between the linear data
# Pearson Correlation: It is defined by R value where R=1 means strong positive relationship and R=-1 means strong negative relationship. R=0 means there is no correlation ( not linearly correlated )

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams
import scipy
from scipy.stats.stats import pearsonr

rcParams['figure.figsize'] = 8,4
plt.style.use('seaborn-whitegrid')

address = 'D:\Repository\DataScience\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

X = cars[['mpg', 'hp', 'qsec', 'wt']]
sb.pairplot(X)
plt.show()

# USE "" SCIPY "" TO CALCULATE THE PEARSON CORRLEATION COEFFICIENT
mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']
pearsonr_coefficient, p_value = pearsonr(mpg, hp) # Looks for the correlation between mpg and hp variable
print('PeasonR Correlation Coefficient %0.3f'% (pearsonr_coefficient))
pearsonr_coefficient, p_value = pearsonr(mpg, qsec)
print('PeasonR Correlation Coefficient %0.3f'% (pearsonr_coefficient))
pearsonr_coefficient, p_value = pearsonr(mpg, wt)
print('PeasonR Correlation Coefficient %0.3f'% (pearsonr_coefficient))

# Use "" PANDA "" to calculate the Pearson R value ( Shortcut). Calculates the R value for each variables
corr = X.corr()

# Use "" Seaborn "" For visualization
sb.heatmap(corr, xticklabels=corr.columns.values, yticklabels= corr.columns.values)
plt.show()
