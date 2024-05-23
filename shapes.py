class Shape:
    def __init__(self):
        
        
class rectangle(Shape):
    def __init__(self, width, height, perimeter, area):
        super().__init__()
        width = int(self.width)
        height = int(self.height)
        perimeter = width*2 + height*2
        area = width*height