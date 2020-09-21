# July 2020
# OBJECCTIVE: BOOLEAN MASKING
import numpy as np
import matplotlib.pyplot as plt

# 1.MAKE ARRAY AND PUT A CONDITION TO GET ANOTHER ARRAY
my_vector = np.array([-17, -4, 0, 2, 21, 37, 105])
print(my_vector)
zero_myvector=0==(my_vector%7)
print(zero_myvector)

sub_array=my_vector[zero_myvector]
print(sub_array)

# 2. ADD ANOTHER CONDITION
sub_array=sub_array[sub_array>7]
print(sub_array)

# 3. MAKE A LOGICAL OPERATOR AND MASK
mod_test=0==(my_vector%7)
positive_test=(my_vector>0)
print(mod_test,'\n',positive_test)
combined_mask=np.logical_and(mod_test,positive_test)
print('Combined:',combined_mask)
print(my_vector[combined_mask])