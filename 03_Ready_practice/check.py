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

# get_icecream


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

def add_sprinkles(func):
    def wrapper():
        print("You added sprinkles")
        func()
    print('Outer1 Ends here')
    return wrapper


def add_choculates(func):
    def wrapper():
        print("You added choculates")
        func()
    print('Outer2 Ends here')
    return wrapper





@add_sprinkles
@add_choculates
def get_icecream():
    print("Here is your icecream")

get_icecream()


######################
# EG4

def add_sprinkles(func):
    def wrapper(*args):
        print("You added sprinkles")
        func(*args)
    print('Outer1 Ends here')
    return wrapper


def add_choculates(func):
    def wrapper(*args):
        print("You added choculates")
        func(*args)
    print('Outer2 Ends here')
    return wrapper





@add_sprinkles
@add_choculates
def get_icecream(flavour):
    print(f"Here is your {flavour} icecream")

get_icecream("Vanilla")



 
