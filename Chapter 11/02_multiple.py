class Parent1:
    a = 34
    
class Parent2:
    b = 20
    
class Child(Parent1, Parent2):
    c = 10
    
ch = Child()
print(ch.a)
print(ch.b)
print(ch.c)

p1 = Parent1()
print(p1.a)
# print(p1.b) # This will give an error
# print(p1.c) # This will give an error  

p2 = Parent2()
# print(p2.a) # This will give an error
print(p2.b) 
# print(p2.c) # This will give an error