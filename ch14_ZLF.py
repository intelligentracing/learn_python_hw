class Shape:
    initiated = False
    def get_area(self):
        pass
    @classmethod
    def is_init(cls):
        return cls.initiated

class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
        self.get_area()
        self.__class__.initiated  = True
    def get_area(self):
        self.area = self.width*self.length
        return self.area

class Square(Shape):
    def __init__(self, width):
        self.width = width
        self.get_area()
        self.__class__.initiated = True  
    def __add__(self,other):
        if self.width == other.width:
            return Rectangle(self.width,self.width*2).area  
    def get_area(self):
        self.area = self.width*self.width
        return self.area
print(Square(3) + Square(3))

