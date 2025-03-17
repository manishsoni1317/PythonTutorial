class Parent:
    a=34
    
class Child1(Parent):
    b=20
    
class Child2(Child1):
    c=10
    
ch2 = Child2()
print(ch2.a)
print(ch2.b)
print(ch2.c)