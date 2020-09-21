# July 2020
# OBJECCTIVE: 1. PLOTING
import math
import collections
import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

# 1. LOAD FROM A FILE
pd.options.display.max_rows = 16
gapminder = pd.read_csv('gapminder.csv')
print(gapminder.head())

# Simple statistic with panda
print(gapminder.describe())

# # create a new Series by doing numpy math on a DataFrame column;
# use dict-like syntax to assign the new Series to a new column in the DataFrame
gapminder['log_gdp_per_day'] = np.log10(gapminder['gdp_per_capita'] / 365.25)
print(gapminder.head())

# to see trend by time
gapminder_by_year = gapminder.set_index('year').sort_index()
# To see trend by country
gapminder_by_country = gapminder.set_index('country').sort_index()

# 2. PLOT: Let's create a plot from year 1960
gapminder_by_year.loc[1960].plot.scatter('log_gdp_per_day', 'life_expectancy')
pp.show()

# 3. SUPERIMPORSE PLOTS: to superimpose multiple Pandas plots, save the axes object returned by the first,
# pass it as "ax" to further plots

axes = gapminder_by_year.loc[1960].plot.scatter('log_gdp_per_day', 'life_expectancy', label=1960)
gapminder_by_year.loc[2015].plot.scatter('log_gdp_per_day', 'life_expectancy', label=2015, color='C1', ax=axes)
pp.show()

# 4. PLOT: AGE OF SURVIVAL WITH YEARS
axes = gapminder_by_year.loc[1960].plot.scatter('log_gdp_per_day', 'age5_surviving', label=1960)
gapminder_by_year.loc[2015].plot.scatter('log_gdp_per_day', 'age5_surviving', label=2015, color='C1', ax=axes)
pp.show()

# 5. PLOT FOR SPECIFIC COUNTRY
gapminder_by_country.loc['Italy'].sort_values('year').plot('year', 'life_expectancy')
pp.show()

# 6. PLOT MULITPLE COUNTRIES
axes = gapminder_by_country.loc['Italy'].sort_values('year').plot('year', 'life_expectancy', label='Italy')
gapminder_by_country.loc['China'].sort_values('year').plot('year', 'life_expectancy', label='China', ax=axes)
gapminder_by_country.loc['United States'].sort_values('year').plot('year', 'life_expectancy', label='USA', ax=axes)

pp.axis(xmin=1900)
pp.ylabel('life expectancy')
pp.show()

# 7. CALCULATE AVERAGE FERTILITY RATE BY TIME
# compute all-countries mean of babies_per_woman after segmenting data by year;
# result is Series indexed by year
gapminder.groupby('year').babies_per_woman.mean()

# 8. TWO AXIS GRAPH
gapminder.groupby('year').babies_per_woman.mean().plot()
pp.ylabel('babies per woman')

# with secondary_y = True, the second plot generate a second set of axis labels
gapminder.groupby('year').age5_surviving.mean().plot(secondary_y=True)
pp.ylabel('age 5 survival [%]')
pp.show()

# 9. CREATE A PIVOT
# pivot table: segment babies_per_woman data by both year and region, then take mean
print(gapminder.pivot_table('babies_per_woman', 'year', 'region'))
gapminder.pivot_table('babies_per_woman', 'year', 'region').plot()
pp.title('babies per woman')
gapminder.pivot_table('age5_surviving', 'year', 'region').plot()
pp.show()