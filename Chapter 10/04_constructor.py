class Employee:
    center = "Not Known"
    def __init__(self, name, salary, center):
        self.name = name
        self.salary = salary
        self.center = center

    def display(self):
        print("Name: ", self.name, ", Salary: ", self.salary, ", Center: ", self.center)
        
emp1 = Employee("John", 1000, "Delhi")
emp2 = Employee("Doe", 2000, "Mumbai")
emp1.display()
emp2.display()