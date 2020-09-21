# July 2020
# OBJECCTIVE: NUMPY BRAIN TEASING QUESTIONS

import numpy as np

# 1. Create a 1D array of numbers from 0 to 9
my_array = np.arange(0, 10)
# print(my_array)

# 2. Q. Create a 3×3 numpy array of all True’s
my_array = np.ones((3, 3), dtype=bool)

# 3. Q. Extract all odd numbers from arr. Desired output: > array([1, 3, 5, 7, 9])
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
my_array = arr[(arr % 2 != 0)]

# 4. Q. Replace all odd numbers in arr with -1. Output: array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2!=0] = -1
# or:
my_array=np.where(arr%2!=0,-1,arr)

# 5. Convert a 1D array to a 2D array with 2 rows
my_array=np.arange(10)
my=np.reshape(my_array,(2,-1)) # -1 automatcially decides the # of columns

# 6. Q. Create the following pattern without hardcoding. Use only numpy functions and the below input array. #> array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
a = np.array([1,2,3])
my_array = np.array([np.repeat(a,3),(np.tile(a,3))]).reshape(1,-1)
# or
my_array = np.array([np.repeat(a,3),(np.tile(a,3))])
my_array=np.concatenate(my_array)
# or
my_array=np.concatenate((np.repeat(a,3),np.tile(a,3)))

# Q7. Get the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
my_array=np.unique(a[a==b]) # Only works if you want to do element by element comparsion.
# or
my_array= np.intersect1d(a,b)

# Q8. Remove specific elements with a condition ( a<2) from an array
a = np.array([1,2,3,2,3,4,3,4,5,6])
#print(np.where(a>3))
my_array = np.delete(a,np.where(a<3),axis=0)


# Q9. From array a remove all items present in array b # > Desired output : array([1,2,3,4])
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9, 1])
my_array = np.setdiff1d(a,b)

# Q10. Get the positions where elements of a and b match. Output: #> (array([1, 3, 5, 7]),)
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
my_array=np.where(a==b)

# Q11. Get all items between 5 and 10 from a.
a = np.array([2, 6, 1, 9, 10, 3, 27])
my_array = a[(a >= 5) & (a <= 10)]
# or
my_array=a[np.all([a >= 5,a<=10],axis=0)]


# Q12. How to make a python function that handles scalars to work on numpy arrays? Get the max elements of arrays and make another array
def maxx(x,y):
    if (x>=y):
        return x
    else:
        return y
# *** Define a vectorized function which takes a nested sequence of objects or numpy arrays as inputs and returns a single numpy array or a tuple of numpy arrays ****

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
my_array = np.vectorize(maxx, otypes=[float])

# print(my_array(a,b))

# Q 13. Swap columns 1 and 2 in the array arr.
arr = np.arange(9).reshape(3,3)
# By using [1,0,2] numpy is just calling specific row numbers. This is not slicing or stepping. It is calling 1 row and then 0 row
my_array=arr[:, [1,0,2]]

# Q14. Swap rows 1 and 2 in the array arr:
my_array=arr[[1,0,2],:]

# Q15. Reverse the rows in the array arr: [start:end:step].
my_array = arr[::-1,:]

# Q16. Reverse the columns in the array arr: [start:end:step].
my_array = arr[:,::-1] # by not defining end and start point it will include all values

# Q17. Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10 + set the number of decimals to 3
my_array=rand_arr = np.random.uniform(5,10, size=(5,3))
np.set_printoptions(precision=3)

# Q18. Limit the number of items printed in python numpy array a to a maximum of 6 elements.
a = np.arange(15)
np.set_printoptions(threshold=6)
#print(a)


print(my_array)




