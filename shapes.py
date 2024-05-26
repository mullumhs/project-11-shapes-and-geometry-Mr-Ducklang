class Shape:
    def __init__(self):
        pass
    
    def perimeter(self):
        pass
    
    def area(self):
        pass
        
class rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = int(width)
        self.height = int(height)
        
        
    def perimeter(self):
        return 2*(self.width + self.height)
        
    def area(self):
        return self.width*self.height
        
class triangle(Shape):
    def __init__(self, base, length, length2):
        super().__init__()
        self.base = int(base)
        self.length = int(length)
        self.length2 = int(length2)
        
    def perimeter(self):
        return self.base + self.length + self.length2
        
    def area(self):
        H = int(input("What is Triangles Height?"))
        return 0.5*(self.base*H)