# July 2020
# OBJECCTIVE: 1. index array elements, 2. Slicing an array, 3. Advanced indexing, 4. Numpy vs Python list indexing and slicing
import numpy as np
import matplotlib.pyplot as plt

# 1. 1D ARRAY INDEX
v = np.linspace(0,10,5)
print(v)
print(v[0])

# 2. 2D ARRAY INDEX : IT IS SIMILAR TO HAVING A LIST WITIHIN A LIST
vv = np.random.random((5,4))
print(vv[(8-4),2])
print(vv[1,2])
my_array= np.arange(35)
my_array.shape = (7,5)


# 3. 1D SLICING
print(v[0:2])

# 4. 2D SLICING
print(vv[2:5,1])
print(vv[2:5,1:2])

# 5. COUNT FROM END
print(vv[2:-1,:])


# 6. STEP THROUGH EVERY 2ND ITEM
print(vv[:,::2])

# 7. NOTE:SLICING AN ARRAY WILL YIELD THE VALUE IN MEMEROY SO IF YOU CHANGE THE SUB-ARRAY IT WILL MODIFY THE ORIGINAL ONE
print('Original:',v)
v2=v[0:2]
print('Tiny:',v2)
v2[1]=0
print('New original:',v)

# SO IF YOU NEED A COPY, YOU NEED TO MAKE IT EXPLICITLY IN NUMPY
v3 = v[2:4].copy()
v3[0] = 10 # Now changing a value will not effect the original file
print(v3,v)

# 8. ADVANCED INDEXING
print(v[[1,2,3]])

# 9. BOOLIAN INDEXING
bool_index = v > 0
print(bool_index)
print(v[bool_index])

# 10. SELECT SPECIAL ELEMENTS
v[v>2]=v[v>2]*2
print(v)

# 11. 3D ARRAY
my_3darray=np.arange(70)
# Two ways to reshape
#Function
my_3darray.shape=(2,7,5)
print(my_3darray)
#Module
mm=my_3darray.reshape((2,7,5))
print(mm)
print(my_3darray[1])
print(my_3darray[1,3])

