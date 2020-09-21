# July 2020
# OBJECCTIVE: 1. DATA FRAME IN PANDA
import pandas as pd
import numpy as np
import collections

# 1. CREATE SERIES: A COLUMN OF THE DATA FRAME
# Series is a type of list in pandas which can take integer values, string values, double values and more. But in Pandas Series we return an object in the form of list, having index starting from 0 to n, Where n is the length of values in series.

# Learn: Create simple series:
author = ['Jitender', 'Purnima', 'Arpit', 'Jyoti']
auth_series=pd.Series(author)
print(auth_series)
# End of learning
pop2015 = pd.Series({'Java': 100,'C': 99.9,'C++': 99.4,'Python': 96.5,'C#': 91.3,'R': 84.8,'PHP': 84.5,'JavaScript': 83.0,'Ruby': 76.2,'Matlab': 72.4})
pop2014 = pd.Series([100,99.3,95.5,93.5,92.4,84.8,84.5,78.9,74.3,72.8],
index=['Java','C','C++','Python','C#','PHP','JavaScript','Ruby','R','Matlab'])

# 2. CREATE SQL OR 2D DATA FRAME
# Series can only contain single list with index, whereas dataframe can be made of more than one series or we can say that a dataframe is a collection of series that can be used to analyse the data.

# Learn: Create simple data frame
author = ['Jitender', 'Purnima', 'Arpit', 'Jyoti']
article = [210, 211, 114, 178]
auth_series = pd.Series(author)
article_series = pd.Series(article)
frame = { 'Author': auth_series, 'Article': article_series }
result = pd.DataFrame(frame)
print(result)
# End of learning

twoyears = pd.DataFrame({'2014': pop2014,'2015': pop2015})
print(twoyears)

# 3. SORT THE DATA
twoyears=twoyears.sort_values('2015',ascending=False)
print('Sorted:\n', twoyears)

# 4. GET THE VALUES
print(twoyears.values)

# 5. GET THE INDEX
print(twoyears.index)

# 6. GET THE COLUMN
print(twoyears.columns)

# 7. GET THE DATA OF A COLUMN
print(twoyears['2014'])

# 8. SELECT A SPECIFIC INDEX BY LOCATION
print(twoyears.iloc[0:2])

# 9. SELECT A SPECIFIC INDEX BY NAME
print('\n',twoyears.loc['C':'Python'])

# 10. FIND THE AVERAGE OF THE DATAFRAME
twoyears['avg']=0.5*(twoyears['2014']+twoyears['2015'])
print('\n',twoyears)

# 11. CREATE A DATA FRAME FROM SCRATCH
presidents = pd.DataFrame([{'name': 'Barack Obama','inauguration': 2009,'birthyear': 1961},
                          {'name': 'George W. Bush','inauguration': 2001,'birthyear': 1946},
                          {'name': 'Bill Clinton','birthyear': 1946,'inauguration': 1993},
                          {'name': 'George H. W. Bush','inauguration': 1989,'birthyear': 1924}])

print(presidents)

# 12. MODIFY THE INDEX FOR SPECIFIC VALUE
presidents_indexes = presidents.set_index('name')
print(presidents_indexes)
print(presidents_indexes.loc['Bill Clinton'])
print(presidents_indexes.loc['Bill Clinton']['inauguration'])

# 13. SUMMARY
SUMMAY=pd.DataFrame(np.random.choice(['a','b','c','d'],(3,3)),index=[1,2,3],columns=['A','B','C'])

print(SUMMAY)

