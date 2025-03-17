class Employee:
    name = "John" # Class attribute
    marks = 80
    center = "Delhi"
    
    def printdetails(self):
        print(f"Name is {self.name}")   
        # return f"Name is {self.name}, marks are {self.marks} and center is {self.center}"
    
    @staticmethod
    def greet():
        print("Good Morning")
    
    
Employee.name = "JohnDo" # Changing the class attribute value
manish = Employee() # Creating an object of Employee class
bittu = Employee() # Creating an object of Employee class
print(manish.name)
print(manish.marks)
print(manish.center)
manish.printdetails()
manish.name = "Manish" # Changing the class attribute value = instance attribute
print(manish.name)
print(bittu.name)
Employee.printdetails(bittu)
bittu.greet()
Employee.greet()