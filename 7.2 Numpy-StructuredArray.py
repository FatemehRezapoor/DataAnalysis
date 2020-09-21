# July 2020
# OBJECCTIVE: CREATE STRUCTURE IN NUMPY
import numpy as np
import matplotlib.pyplot as plt

# 1.MAKE STRUCTURED ARRAY
person_data_def = [('name','S6'),('height','f8'),('weight','f8'), ('age', 'i8')]
# s means it is string, f is float, and i is integer
print(person_data_def)

# 2. MAKE ARRAY LIKE STRUCUTRED ARRAY
people_array = np.zeros((4,), dtype=person_data_def) # Means the array has a data type equal to our person array data variations
print(people_array)
people_array[0] = ('Alpha', 65, 112, 23)
people_array[3] = ('Delta', 73, 205, 34)
print(people_array)

ages = people_array['age']
print(ages)

# 3. USE TO CREATE STRUCTURED ARRAYS
people_big_array = np.zeros((4,3,2), dtype=person_data_def)
people_big_array[3,2,1] = ('Echo', 68, 155, 46)
print(people_big_array)
print(people_big_array['height'])

# 4. CREATE RECORD ARRAY
person_record_array = np.rec.array([('Delta', 73, 205, 34),('Alpha', 65, 112, 23)],dtype=person_data_def)
print(person_record_array)
print(person_record_array[0].age)

