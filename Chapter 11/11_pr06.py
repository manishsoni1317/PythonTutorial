class Vector2d:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def printVector(self):
        print(f"{self.x}x + {self.y}y")
        
class Vector3d(Vector2d):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        
    def __str__(self):
        return f"{self.x}x + {self.y}y + {self.z}z"
        
   
v3 = Vector3d(11, 5, 9)   
print(v3)

