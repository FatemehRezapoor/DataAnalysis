# August 2020
# OBJECCTIVE: STATISTICAL CALCULATIONS

import numpy as np
from numpy.random import randn

# CREATING ARRAYS
np.set_printoptions(precision=2)
a=np.array([1,2,3,4,5,6])
b=np.array([[10,20,20],[40,50,60]])
print('a\n',a,'\nb\n',b)

# CREATE ARRAY VIA ASSIGNMENT
np.random.seed(25) # seed reproduce the data
c = 36*np.random.randn(6)
d=np.arange(1,35)

print('c\n',c,'\nd\n',d)

# PERFORM MATH ON ARRAYS
print('a*10+c:\n',a*10+c)
print('c/a\n',c/a)

# PERFORMING MULTIPLYING WITH MATRICES AND LINEAR ALGEBRA
aa = np.array([[2.,4.,6.],[1.,3.,5.],[10.,20.,30.]])
bb = np.array([[0.,1.,2.],[3.,4.,5.],[6.,7.,8.]])
print('aa*bb\n',aa*bb)
print('Dot product\n',np.dot(aa,bb))

