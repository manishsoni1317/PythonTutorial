class Employee:
    a = 34
    b = 4
    c = 10
    
    @classmethod
    def setAttr(cls,a,b,c):
        cls.a = a
        cls.b = b
        cls.c = c
        
    @property
    def length(self):
        return self.a
    
    @length.setter
    def length(self,value):
        self.a = value
        
emp = Employee()
emp.setAttr(100,200,300)
print(emp.length)
emp.length = 500
print(emp.length)