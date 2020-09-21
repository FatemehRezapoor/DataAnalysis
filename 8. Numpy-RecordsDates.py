# July 2020
# OBJECCTIVE: 1. Create a record in numpy, 2. Use date and time
import numpy as np
import matplotlib.pyplot as plt

# 1. CREATE RECORD: INCLUDES LIST + DIC IN A TUPIL
reca = np.array([(1,(2.0,3.0),'hey'),
                 (2,(3.5,4.0),'n')],
                dtype=[('x',np.int32),('y',np.float64,2),('z',np.str,4)])
print(reca)

# Access first row
print(reca[0])

# Access first column
print(reca['x'])

# Access specific row and column
print(reca[0]['x'])

# 2. DATE AND TIME
print(type(np.datetime64('2015')))
print(np.datetime64('2015-02-03 12:00:00'))

# Compare date and time
print(np.datetime64('2015-01-01')<np.datetime64('2015-05-01'))

# Math on date and time
print(np.datetime64('2015-04-03') - np.datetime64('2015-01-01'))
print(np.datetime64('2015-04-03') + np.timedelta64(5,'D')) # Add days
print(np.datetime64('2015-04-03') + np.timedelta64(5,'h')) # Add hours

# Convert date time to numbers
print(np.datetime64('2015-01-01').astype(float)) # It presents the number of days since 1970 which is a standard date. 1st January 1970' usually called as "epoch date" is the date when the time started for Unix computers, and that timestamp is marked as '0'. Any time since that date is calculated based on the number of seconds elapsed
print(np.datetime64('1970-01-01').astype(float))

# Build array
r = np.arange(np.datetime64('2016-02-01'),np.datetime64('2016-03-01'))
print(r)





