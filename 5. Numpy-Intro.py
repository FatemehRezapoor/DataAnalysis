# July 2020
# OBJECCTIVE: 1. Create arrays, 2. Find type and shape of arrays, 3. compose arrays, 4. Load and save arrays
import numpy as np
import matplotlib.pyplot as pp
print(np.__version__)
# 1. CREATE AN ARRAY
a= np.array([1,2,3,4,5])
print(a)
# Compare with list
l=[1,2,3,4,5]
print('L*2: ',l*2)
print('l+l: ',l+l)
al=np.array(l)
print('al*2: ',al*2)

# CREATE ARRAY FROM TUPLE
mytuple=(14,-3.54,5+7j)
mytuple_array=np.array(mytuple)
print(mytuple_array*2)

# 2. PRINT ARRAY TYPE
print(a.dtype)

# 3. CHANGE THE ARRAY TYPE
a=np.array([1,2,3],dtype=np.float64)
print(a)

# 4. COMMON ATTRIBUTES: DIM , SHAPE , SIZE: Number of elements
print(a.ndim, a.shape, a.size)
print(a.itemsize) #Length of one array element in bytes.

# 5. 2D ARRAY
b = np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype=np.float64)
print(b)
print(b.ndim, b.shape, b.size)

# 6. ZERO & ONE ARRAY
myzero=np.zeros((3,3),'d') # 'd' stands for double array type
print(myzero)
my3d_one=np.ones((2,1,5)) # means we have two array of 1x5 size
print(my3d_one)

# 7. EMPTY ARRAYS
myempty= np.empty((4,4),'d')
print(myempty)

# 8. SPACED ARRAYS :
# CREATE ARRAYS WITH EQUAL SPACED INTERVALS. Similar to arrange function, it uses number of samples instead of step size. Includes stop parameter too. 9 means we want 9 samples in 0-10 interval
print(np.linspace(0,10,9))
# To find the step size
my_linespace= np.linspace(0,10,9,retstep=True)
print(my_linespace[1])

# 9. RANGE OF ARRAYS
print(np.arange(0,10,2))
print(np.arange(25,step=5))

# 10. RANDOM NUMBERS
print(np.random.standard_normal((2,4)))

# 11. COMBINE ARRAYS/STACKING
a=np.random.standard_normal((2,3))
b=np.random.standard_normal((2,3))

# Vertical Stack
print(np.vstack([a,b]))
# Horizental stack
print(np.hstack([a,b]))

# 12. TRANSPOSE ARRAYS
print(a.transpose())

# 13. SAVE ARRAYS
am=np.array([1,2,3,4,5,6])
np.save('myarray.npy',am)

# 14. READ SAVED ARRAY
print(np.load('myarray.npy'))

