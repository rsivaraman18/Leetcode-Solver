# Iterators Learning



#### Example 1 - __iter__ ,__next__
# numbers = [1,4,6,]
# value = numbers.__iter__()
# item1 = value.__next__()
# item2 = value.__next__()
# item3 = value.__next__()
# # item4 = value.__next__()
# print('item1: ',item1)
# print('item2: ',item2)
# print('item3:',item3)
# print('item4:',item4) ## StopIteration



# ### Exampe 2 -iter,next
# numbers = [1,4,6]
# value = iter(numbers)
# item1 = next(value)
# item2 = next(value)
# item3 = next(value)
# print('item1: ',item1)
# print('item2: ',item2)
# print('item3:',item3)


# ### Example 3 - Working of for Loop
# numbers = [1,4,6]
# iter_obj = iter(numbers)

# while True:
#     try:
#         element = next(iter_obj)
#         print(element)
#     except StopIteration:
#         break


# class Even:
#     def __init__(self,maximum):
#         print("Init Method")
#         self.n = 2
#         self.maximum = maximum
    
#     # def __iter__(self):
#     #     print("Iter Method")
#     #     return self

#     def __next__(self):
#         if self.n <= self.maximum:
#             print("Next if Method")
#             result = self.n
#             self.n += 2
#             return result
        
#         else:
#             print("Else if Method")
#             raise StopIteration

# numbers = Even(6)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# def even_generator():
#     n =0
#     n += 2
#     yield n
#     n += 2
#     yield n
#     n += 2
#     yield n

# value = even_generator()
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))

# import sys
# mylist = [1,2,3,4,5,6,7,8,9,10]
# print(sys.getsizeof(mylist))
# print(sys.getsizeof(range(1,11))) 

# x = map(lambda i :i**2 ,mylist)
# y = list(x)
# print(sys.getsizeof(x))
# print(sys.getsizeof(y))


squares_generator = (i * i for i in range(5))
print(squares_generator)