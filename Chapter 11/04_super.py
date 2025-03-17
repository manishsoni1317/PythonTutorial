class Parent:
    a=34
    def __init__(self) -> None:
        print("Parent class constructor")
    
class Child1(Parent):
    b=20
    def __init__(self) -> None:
        print("Child1 class constructor")
        super().__init__()
    
class Child2(Child1):
    c=10
    def __init__(self) -> None:
        super().__init__()
        print("Child2 class constructor")
    
ch2 = Child2()
print(ch2.a)
print(ch2.b)
print(ch2.c)