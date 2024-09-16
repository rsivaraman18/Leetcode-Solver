# import check2
# print("check3 ")
# print(check2.callme())
# print(check2.Greet)

# print('Check3:',__name__)

###### 
# numbers = [1,2,11,22]

# def square(x):
#     if x >10:
#         return x**2
#     else:
#         return x**3
    
# greater = list( map(square, numbers))
# big     = list(filter(square , numbers))

# print('greater',greater)
# print('big',big)


### REDUCE

# from functools import reduce
# numbers = [1,2,3,4,5]
# numbers2 = [1,2,3,4,5]

# def addition (x,y,z):
#     return x+y+z

# total = reduce(addition,numbers,numbers2)
# print(total)

from functools import reduce
L = [1,2,43,4,5,10,23,15,7]
m = reduce(lambda x,y : x if x>y else y , L)
print(m)


""" Hello functools"""
# print(__doc__)

def caller():
    "sadsad"
# print(dir())
print(__doc__) 

"""
This module demonstrates the use of __doc__.
"""
import pandas as pd
print(__doc__)  # Prints the module-level docstring
print(__package__)
