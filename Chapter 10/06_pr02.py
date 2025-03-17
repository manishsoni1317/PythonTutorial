import math


class Calculator:
    def __init__(self, number):
        self.number = number
        
    def square(self):
        return self.number ** 2
    
    def squareRoot(self):
        return math.sqrt(self.number) 
    
    def cube(self):
        return self.number ** 3

    def add(self, number):
        self.number += number
        return self.number

    def sub(self, number):
        self.number -= number
        return self.number
    
two  = Calculator(2)
print(two.square())
print(two.squareRoot())
print(two.cube())
print(two.add(2))
print(two.sub(2))