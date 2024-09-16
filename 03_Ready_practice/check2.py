

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

    
obj = Greet("Siva")
print(obj.wish())

# print(dir())
print('Check2:',__name__)



