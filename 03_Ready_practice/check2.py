

def callme():
    print("I am ready to make call")

def hangup():
    print("I am ready to close the call")



class Greet:


    def __init__(self,name) :
        print("I am Constructor")
        self.name = name

    def wish(self):
        return f"Good Morning {self.name}"

    
# obj = Greet("Siva")
# print(obj.wish())

# # print(dir())
# print('Check2:',__name__)


######################

# L = [lambda x :x**2 , lambda x :x**3]
# for f in L:
#     print(f(3))


######

l = [n for n in range(5)]
f = lambda x : bool(x%2)
print(f(3),f(1))  ### True True

for i in range(len(l)):
    
    if f(l[i]):
        del l[i]
        print(i)


