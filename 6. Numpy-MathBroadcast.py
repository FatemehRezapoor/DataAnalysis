# July 2020
# OBJECCTIVE: 1. Create arrays, 2. Find type and shape of arrays, 3. compose arrays, 4. Load and save arrays
import numpy as np
import matplotlib.pyplot as plt

# 1. CREATE LINESPACE
x = np.linspace(0,10,40)
print(x)

# 2. CREATE SIN FUNCTION
sinx=np.sin(x)
plt.plot(x,sinx)
#plt.show()

# 3. CREATE COS FUCNTION
cosx=np.cos(x)
plt.plot(x,cosx)
#plt.show()

# 4. PLOT IN ONE SIDE BY SIDE GRAPH
plt.subplot(2,1,1)
plt.plot(x,sinx)
plt.title('Two Graph')
plt.ylabel('Sin')

plt.subplot(2,1,2)
plt.plot(x,cosx,'ro')
plt.xlabel('x Value')
plt.ylabel('Cos')

#plt.show()

# 5. PLOT IN ONE GRAPH

plt.plot(x,sinx,'x')
plt.plot(x,cosx,'ro')
plt.legend(['sin(x)','cos(x)'])
#plt.show()

# 6. INNER & OUTER PRODUCT
mandot=np.dot(sinx,cosx)
print(mandot)
mnaout=np.outer(sinx,cosx)
print(mnaout)

# 7. ADD A NUMBER TO ARRAY
a=np.array([1,2,3])
print(a+1)

# 8. ADD A 1D ARRAY TO 2D ARRAY ( Rows )
c=np.vstack([a,a])
print('Rows',a+c)

# 9. 3D ARRAY
my_3D_array = np.arange(70).reshape(2,7,5)
print(my_3D_array)
# SUMMATION OF ALL ELEMENTS
print(my_3D_array.sum())
# SUMMATIN ALONG THE AIXS
# Options are axis = 0,1,2 that each of them depends on the array dimension.

# NOTE: FOR 2D ARRAY, AXIS = 0 MEANS SUMMATION ALONG THE COLUMNS AND AXIS = 1 MEANS SUMMATION ALONG THE ROWS.
# NOTE: FOR 3D ARRAY, AXIS=0 MEANS SUMMATION ALONG THE COLUMNS OF ALL ARRAYS => RESULT IS 7*5 ARRAY
# AXIS = 1 MEANS SUMMATION ALONG THE COLUMN OF EACH INDVIDUAL ARRAY => RESULT IS 2*5
# AND AXIS = 2 MEANS SUMMATION ALONG THE EACH INDIVIDUAL ROW => RESULT IS 2*7
print(my_3D_array.sum(axis=2))

# 10. BROADCASTING
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]])
b=a*2
print('a:\n',a,'\nb:\n',b)
print('a*b:\n',a*b)
print('a/b:\n',a/b)
c=np.array([10,10,10])
print(a/c)
