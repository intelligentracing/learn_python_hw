#Author:Yu Qiushuang

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
#ex1.1
class Rectangle(Shape):
    ''' A subclass of Shape, specifically for calculating rectangle area'''

    def __init__(self,width,length):
        self.width = width
        self.length = length
        self.get_area()
        self.__class__.initiated = True

    def get_area(self):
        ''' Area of a rectangle is its width times length'''
        self.area = self.width * self.length
        return self.area
#######################Rectangle calss test start###################################
# s = Rectangle(6,8)

# print(s.is_init())
# print(s.get_area())
#######################Rectangle class test end######################################

#ex1.2
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


#######################Square class test end######################################
s1 = Square(8)
s2 = Square(8)

enroll = s1 + s2
print(s1.get_area())
print(enroll.get_area())
######################Square class test end######################################






