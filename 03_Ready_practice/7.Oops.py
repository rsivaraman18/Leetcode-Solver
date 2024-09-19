### LEARN STATIC METHOD
### Example 1
# class Calculator:
#     def __init__(self,version) :
#         self.version = version

#     def description(self,):
#         print(f"Current Calculator Version is {self.version}")

#     def add_numbers(self,*numbers):
#         return sum(numbers)
    
#     def addition_numbers(*numbers):
#         print("Static Method Called , Even can be placed outside the Class")
#         return sum(numbers)

# if __name__ =="__main__":
#     cal1 = Calculator(10)
#     cal2 = Calculator(100)

#     cal1.description()
#     cal2.description()

#     print(cal1.add_numbers(10,20.30))
#     print(cal2.add_numbers(6,36,54))

#     print(Calculator.addition_numbers(10,20.30))
    

### Example 2 : Class Method
from datetime import date

class AgeCalcuator:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def description(self,):
        print(f"{self.name} age is {self.age} years")

    @classmethod
    def age_from_year(cls,name,birth_year):
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name,age)
    

# myage = AgeCalcuator("Raj",1995)
# myage.description()

obj = AgeCalcuator.age_from_year('raj',1997)
print(obj.description())
    

