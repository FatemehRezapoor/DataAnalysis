# July 2020
# OBJECCTIVE: 1. SCIPY: a collection of numerical algorithms and domain-specific toolboxes, including signal processing, optimization, statistics, and much more.
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import norm

number_of_data_points = 99
a = sp.randn(number_of_data_points)
print(type(a))

# 1. CALCULATE MEAN
print(a.mean())

# 2. CALCULATE MEDIAN
print(sp.median(a))

# 3. CALCULATE MAX AND MIN
min_max= np.array([[a.min()],[a.max()]])
print(min_max)

# 4. CALCULATE STANDARD DEVIATION + VARIANCE
spread_measures = np.array([sp.std(a), sp.var(a)])
print(spread_measures)

# 5. HIGH LEVEL INFORMATION
print(sp.stats.describe(a))

