### LEARN STATIC METHOD

class Calculator:
    def __init__(self,version) :
        self.version = version

    def description(self,):
        print(f"Current Calculator Version is {self.version}")

    def add_numbers(self,*numbers):
        return sum(numbers)
    
    def addition_numbers(*numbers):
        print("Static Method Called , Even can be placed outside the Class")
        return sum(numbers)

if __name__ =="__main__":
    cal1 = Calculator(10)
    cal2 = Calculator(100)

    cal1.description()
    cal2.description()

    print(cal1.add_numbers(10,20.30))
    print(cal2.add_numbers(6,36,54))

    print(Calculator.addition_numbers(10,20.30))
    