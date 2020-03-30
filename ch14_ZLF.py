class Shape:
    ''' An example class that defines an empty abstract shape '''
    initiated = False

    def get_area(self):
        ''' virtual method to calculate area of a shape'''
        pass

    @classmethod
    def is_init(cls):
        ''' return True if a shape has been assigned to the class'''
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
    ''' A subclass of Shape, specifically for calculating square area'''

    def __init__(self, width):
        self.width = width
        self.get_area()
        self.__class__.initiated = True  

    def __add__(self,other):
        if self.width == other.width:
            print( Rectangle(self.width,self.width*2).area  )  
    
    def get_area(self):
        ''' Area of a square is its width times width'''
        self.area = self.width*self.width
        return self.area


Square(3) + Square(3)

