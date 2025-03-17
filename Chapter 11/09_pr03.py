class Employee:
    def __init__(self, salary, increment) -> None:
        self.salary = salary
        self.increment = increment
    
    @property    
    def salaryAfterIncrement(self):
        return self.salary + self.increment
    
        
emp1 = Employee(1000, 200)
print(emp1.salary)
print(emp1.salaryAfterIncrement)