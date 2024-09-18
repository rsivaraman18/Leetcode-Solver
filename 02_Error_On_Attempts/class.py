class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)


# ###
#  isinstance(miles, Bulldog)
# False

# >>> isinstance(miles, Dog)
# False

# >>> isinstance(buddy, Bulldog)
# True

# >>> isinstance(jack, Dog)
# False

# >>> isinstance(jack, Dachshund)
# False

# >>> isinstance(miles, Dog)
# True