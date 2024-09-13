def add_sprinkles(func):
    def wrapper():
        print("You added sprinkles")
        func()
    print('Outer Ends here')
    return wrapper


@add_sprinkles
def get_icecream():
    print("Here is your icecream")

get_icecream


####################################

