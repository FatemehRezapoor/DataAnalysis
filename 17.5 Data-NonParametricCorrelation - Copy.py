# September 2020
# OBJECCTIVE: NonParametric Corrolation: Find the relation between the nonlinear data, non normally distributed and categorial data
# Spearman's rank Correlation: It is related to the ordinal data ( Kind of categorail data with the set order or scale to it ( like 1-10)).
# Spearman finds the R for ordinal data and determines the strength of corrolation. R=1 means strong positive relationship, R = = not correlation and R=-1 strong negative relationship. Assumptions: Variables are ordinal and nonlinearly related and non normally distributed
# Chi - Square: Determines the independence of variables. The null hypothesis is that the variables are independent of one another. So P<0.05 Rejects the null hypothesis and concludes that the variables are correlated, P>0.05 accepts the null and conclude that the variables are independent. Use Chi-square for categorial or numeric. In case of numerical values, make sure they are binned.

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats import spearmanr

rcParams['figure.figsize'] = 14,7
plt.style.use('seaborn-whitegrid')

address = 'D:\Repository\DataScience\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

sb.pairplot(cars)
#plt.show()


X = cars[['cyl', 'vs', 'am', 'gear']]
sb.pairplot(X)
plt.show() # Shows the variables are nonlinearly related

# Let's isolate the values
cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']

# Calculate the Spearman R coefficient
spearmanr_coefficient, p_value = spearmanr(cyl, vs)
print('Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient))
spearmanr_coefficient, p_value = spearmanr(cyl, am)
print('Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient))
spearmanr_coefficient, p_value = spearmanr(cyl, gear)
print('Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient))

# Chi-square test for independence
# 1. Create a cross tab
table = pd.crosstab(cyl, am)
# 2. import chi2 function
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(table.values)
print ('Chi-square statistic %0.3f p_value %0.3f' % (chi2, p))

table = pd.crosstab(cyl, vs)

from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(table.values)
print ('Chi-square statistic %0.3f p_value %0.3f' % (chi2, p))

table = pd.crosstab(cyl, gear)

from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(table.values)
print ('Chi-square statistic %0.3f p_value %0.3f' % (chi2, p))