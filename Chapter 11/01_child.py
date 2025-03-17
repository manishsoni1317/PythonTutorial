class Employee:
    a = 34
    

class Child(Employee):
    b = 20

ch = Child()    
print(ch.a)
print(ch.b)

em = Employee()
print(em.a)
# print(em.b) # This will give an error
