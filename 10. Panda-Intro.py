# July 2020
# OBJECCTIVE: 1. Make series objectives from lists and dicts, 2. Extracting indexes and values, 3. Indexing series objects implicitly and explicitly
# Fast data cleaning + prepaeration + analysis+ data visualizatoin and ML.
import pandas as pd

# 1. CREATE SERIES: One-dimensional ndarray with axis labels (including time series).
s = pd.Series([0,1,4,9,16,25],name='squares')
print(s)

# 2. GET VALUES
print(s.values)

# 3. GET INDEX
print(s.index)
print(s[2])
print(s[2:4])

# 4. Example : Index defiend in left and value in the right
pop2014 = pd.Series([100,99.3,95.5,93.5,92.4,84.8,84.5,78.9,74.3,72.8],
                    index=['Java','C','C++','Python','C#','PHP','JavaScript','Ruby','R','Matlab'])
print(pop2014)
print(pop2014.index)
print(pop2014[0:2])
print(pop2014['Python'])
print(pop2014['C++':'C#'])
print(pop2014[pop2014 > 90])

# 5. ANOTHER METHOD TO CREATE SERIES
pop2015 = pd.Series({'Java': 100,'C': 99.9,'C++': 99.4,'Python': 96.5,'C#': 91.3,'R': 84.8,'PHP': 84.5, 'JavaScript': 83.0, 'Ruby': 76.2, 'Matlab': 72.4})
print(pop2015)