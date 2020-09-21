# July 2020
# OBJECCTIVE: 1. VIEWS AND COPIES
import numpy as np
import matplotlib.pyplot as plt

# 1. CREATE ARRAYS AND CHECK IF THEY ARE THE SAME OR DIFFERENT?
my_house = np.array([-45, -31, -12, 0, 2, 25, 51, 99])
your_house=my_house

# check equality
print(your_house is my_house)
# check id
print(id(my_house),id(your_house))
# Check value equality
print(your_house==my_house)

your_house[4]=1010
print(my_house,your_house)
print(your_house is my_house)
# Note: CHANGING THE CHILD ARRAY CHANGES THE PARENT ARRAY

# 2. COPY
your_house=np.copy(my_house)
your_house[4]=555
print(my_house,your_house)

# ADD ELEMENTS TO ARRAY
a = np.array(np.arange(24)).reshape(2,3,4)
b=np.append(a,[5,6,7,8])
print('a\n',a,'\n','b\n',b)

# 3. CANCATENATE
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6],[7,8]])
together = np.concatenate((a, b), axis=0)
print(together)
together = np.concatenate((a, b), axis=1)
print(together)

# 4. STACK/SPLIT ???

#5. FLIP
print(np.fliplr(a))
print(np.flipud(a))

# 6. ROLL: Elements that roll beyond the last position are re-introduced at the first OR TO THE END

my_array = (np.array(np.arange(24))).reshape((3,8))
print(my_array)
print(np.roll(my_array,5))
print(np.roll(my_array,-5))

# 7. ROTATION:
print(np.rot90(np.array([[1,2],[3,4],[5,6]]))) # Counter CW
print(np.rot90(np.array([[1,2],[3,4],[5,6]]),k=-1)) # Counter CW

# 8. TRANSPOSE
print(np.transpose(np.array([[1,2],[3,4],[5,6]])))

# 9. TILE: Replicate
at=np.arange(6)
att=np.tile(at,2)
print(att)

# 10. REPEAT: EACH ELEMENTS REPEAT ITSELF
atr=np.repeat(at,2)
print(atr)