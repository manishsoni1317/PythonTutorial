class Employee:
    a = 34
    b = 4
    c = 10
    
    @classmethod
    def setAttr(cls,a,b,c):
        cls.a = a
        cls.b = b
        cls.c = c
        
emp = Employee()
print(emp.a)
print(emp.b)
print(emp.c)
emp.setAttr(100,200,300)
print(emp.a)
print(emp.b)
print(emp.c)