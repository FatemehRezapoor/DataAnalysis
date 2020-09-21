# July 2020
# OBJECCTIVE: 1. Sympy: SymPy is a Python library for symbolic mathematics (Linear algebra). It aims to become a full-featured computer algebra system (CAS) while keeping the code as simple as possible in order to be comprehensible and easily extensible. SymPy is written entirely in Python.
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy import init_session
my_teaser_array = np.array([1, 7, 19, 37, 61, 91, 127, 169, 217, 271, 331])

# 1. Diff in numpy: Substracts the elements
print('Onee time: ',np.diff(my_teaser_array))
print('Two times',np.diff(my_teaser_array,2))
print('Three times',np.diff(my_teaser_array,3))

# 2. DIFF in sympy
from sympy import init_session
# init_session() # Create interactive platform
x=sym.Symbol('x')
print(sym.diff(x**3))
print(sym.diff(x**3,x,3))



