class Employee:
    name = "John"
    marks = 80
    center = "Delhi"
    
    def printdetails(self):
        print(f"Name is {self.name}")   
        # return f"Name is {self.name}, marks are {self.marks} and center is {self.center}"
    
manish = Employee() # Creating an object of Employee class
print(manish.name)
print(manish.marks)
print(manish.center)
manish.printdetails()