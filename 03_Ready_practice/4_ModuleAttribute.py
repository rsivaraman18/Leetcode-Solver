# """ __name__  Module"""
# import math
# # print('math.__name__ : ',math.__name__)

# # print('__name__ :',__name__)



# ##############
# """__file__ --> Give Current File Location/Absolute Path"""
# # print("__file__ :,",__file__)



# #############################

# """__doc__  DOCSTRING DETAILS"""
# # print("__doc__ : ",__doc__) #  __name__  Module




# ###########################
# """ __dict__  Module"""

# import math
# # print(math.__dir__())
# import random


# #######
# """dir() -- Gives all Class,functions,Modules,package used in that python file"""
# number = [1,2,3,34,]
# # print(dir())

# ####
# import keyword
# # print(keyword.kwlist)
# # print(len(keyword.kwlist))

# # print(dir(math))

# # print(2**0)
# # print(2**1)
# # print(int(0x8E))

# ### Convert Number to Binary

# # number = 100
# # result = ''
# # while number>1:
# #     q = number//2
# #     r = number % 2
# #     number = q
# #     result = str(r) + result 
    
# # result = '1'+ result
# # print(f"Number {number} to Binary Value is {result}")

# # ### Convert Binary to Number
# # bin_value = 1100100
# # bin_value = str(bin_value)
# # number = 0
# # power = 0

# # a = [1, 2, 3]
# # b = a[:]
# # print(b)
# # b.append(4)
# # print(a)
# # print(b)

# # a = 'Hello'
# # b = 'Hello'
# # c = a
# # d = 'H'
# # print("a:",id(a)) 
# # print("b:",id(b)) 
# # print("c:",id(c)) 
# # print("d:",id(d)) 

# # num1 = int(2.3)
# # print(num1)  # prints 2

# # num2 = int(-2.8)
# # print(num2)  # prints -2

# # num3 = float(5)
# # print(num3) # prints 5.0

# # num4 = complex('3+5j')
# # print(num4)  # prints (3 + 5j)

# # print(float((3 + 5j)))
# # print(complex(0.7))
# # import math
# # print(dir(math))

# print(bool(None))  # Output: False
# print(bool(0))    # Output: False
# print(bool(0.0))  # Output: False

# print(bool([])) 
# print(bool(())) 
# print(bool({})) 
# print(bool("")) 
# print(bool(set())) 
# print(bool(False)) 

# class MyClass:
#     def __bool__(self):
#         return False

# obj = MyClass()
# print(bool(obj))  

# class AnotherClass:
#     def __len__(self):
#         return 0

# obj = AnotherClass()
# print(bool(obj))  # Output: False



# print(bool([]))
# print(bool())

# class Truth:
#     pass

# x = Truth()
# print(bool(x))

# print(4&5)

name = "    hello  herterer "
# print(len(name))
# d = name.strip()
# print(len(d))

# print(40>>2)
# print(12>>2)
# print(27>>2)

import math
x = 3.4
y = 2.8
# print(math.ceil(x))
# print(math.ceil(y))
# print(math.floor(x))
# print(math.floor(y))
# a = -3.4
# b = -2.8
# print('Math Ceil floor')
# print(math.ceil(a))
# print(math.ceil(b))
# print(math.floor(a))
# print(math.floor(b))

number = 1999.565565
# print(round(number))

a = ['orange','mango','kiwi','guava','mango','pine','mango']
b = a.index('mango',2)
# print(b)

# print(dir(list))
"""
1.LIST METHODS
    'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 
    'remove', 'reverse', 'sort'
2.TUPLE
    'count','index'
3.SET
    'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'update'
    'pop', 'remove', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
    'issuperset','symmetric_difference', 'symmetric_difference_update', 'union', 

4.DICT METHODS
    clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

5.STRIMG
    'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
    'find', 'format', 'format_map', 'index', rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
    'strip', 'swapcase', ''title', 'translate', 'upper', 'zfill','replace', 'rfind', 'rindex', 'rjust',
    'rpartition','partition', 'join', 'ljust', 'lower', 'lstrip','removeprefix', 'removesuffix', 
    'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
    'isspace', 'istitle', 'isupper',  'maketrans', 
    
    
"""
# lst = [[3,14],[4,7]]
# print(sum(lst,5))

# a = [2,3,7]
# print(sum(a,[7]))


# a = {1,2,3,4}
# b = {5,2,6,7}
# c = {5,6,7}
# d = {1,2}


# print(a.intersection(b))
# print(a.intersection_update(b))



a = type(0x101)
print(a)


text = "   Hello World   "
result = text.strip()
print(result)  # Output: "Hello World"

# Removing specific characters
text = "###Pyt#hon###"
result = text.strip('#')
print(result)  # Output: "Python"





