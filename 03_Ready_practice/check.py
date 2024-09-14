#Example 1 : 

# def add_sprinkles(func):
#     def wrapper():
#         print("You added sprinkles")
#         func()
#     print('Outer Ends here')
#     return wrapper


# @add_sprinkles
# def get_icecream():
#     print("Here is your icecream")

# get_icecream()


####################################
#Example 2 : Withou inner Function

# def add_sprinkles(func):
    
#     print("You added sprinkles")
#     func()


# @add_sprinkles
# def get_icecream():
#     print("Here is your icecream")

# get_icecream



####################################
# Example3:

# def add_sprinkles(func):
#     def wrapper():
#         print("You added sprinkles")
#         func()
#     print('Outer1 Ends here')
#     return wrapper


# def add_choculates(func):
#     def wrapper():
#         print("You added choculates")
#         func()
#     print('Outer2 Ends here')
#     return wrapper





# @add_sprinkles
# @add_choculates
# def get_icecream():
#     print("Here is your icecream")

# get_icecream()


######################
# EG4

# def add_sprinkles(func):
#     def wrapper(*args):
#         print("You added sprinkles")
#         func(*args)
#     print('Outer1 Ends here')
#     return wrapper


# def add_choculates(func):
#     def wrapper(*args):
#         print("You added choculates")
#         func(*args)
#     print('Outer2 Ends here')
#     return wrapper





# @add_sprinkles
# @add_choculates
# def get_icecream(flavour):
#     print(f"Here is your {flavour} icecream")

# get_icecream("Vanilla")

#################
# Example 6
# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner


# def ordinary():
#     print("I am ordinary")

# # Output: I am ordinary


####################
# Example 5:
# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return

#         return func(a, b)
#     return inner

# @smart_divide
# def divide(a, b):
#     print(a/b)

# divide(2,5)

# divide(2,0)


########### Example 7

# def star(func):
#     def inner(*args, **kwargs):
#         print(11111111)
#         func(*args, **kwargs)
#         print(2222222)
#     print('star 1')
#     return inner


# def percent(func):
#     def inner(*args, **kwargs):
#         print(3333333)
#         func(*args, **kwargs)
#         print(444444)
#     print('percent 2')
#     return inner


# @star
# @percent
# def printer(msg):
#     print(msg)

# printer("Hello")


##### Example 7
# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#     return multiplier


# # Multiplier of 3
# times3 = make_multiplier_of(3)

# # Multiplier of 5
# times5 = make_multiplier_of(5)

# # Output: 27
# print(times3(9))

# # Output: 15
# print(times5(3))

# # Output: 30
# print(times5(times3(2)))

### Example 8
# def greet(name):
#     return f"Hello & Welcome {name}"

# gm = greet("Python")

######### Example 9




 
