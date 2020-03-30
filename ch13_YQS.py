class Shape:
    ''' An example class that defines an empty abstract shape '''
    initiated = False  # 记录shape是否已经被定义为某个形状

    def get_area(self):
        ''' virtual method to calculate area of a shape'''
        pass

    @classmethod
    def is_init(cls):
        ''' return True if a shape has been assigned to the class'''
        return cls.initiated


class Square(Shape):
    ''' A subclass of Shape, specifically for calculating square area'''

    def __init__(self, width):
        self.width = width
        self.get_area()
        self.__class__.initiated = True

    def get_area(self):
        ''' Area of a square is its width times width'''
        self.area = self.width * self.width
        return self.area

    def __add__(self, other):
        if self.width == other.width:
            rect = Rectangle(self.width, self.width * 2)
            return rect
        else:
            return None

class Rectangle(Shape):
    ''' A subclass of Shape, specifically for calculating rectangle area'''

    def __init__(self,width,length):
        self.width = width
        self.length = length
        self.get_area()
        self.__class__.initiated = True

    def get_area(self):
        ''' Area of a rectangle is its width times width'''
        self.area = self.width * self.length
        return self.area

