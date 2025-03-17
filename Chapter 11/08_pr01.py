class Vector2d:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def printVector(self):
        print(f"{self.x}i + {self.y}j")
        
class Vector3d(Vector2d):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        
    def printVector(self):
        print(f"{self.x}i + {self.y}j + {self.z}k")
        
v2 = Vector2d(1, 5)        
v3 = Vector3d(1, 5, 9)   

v2.printVector()
v3.printVector()
