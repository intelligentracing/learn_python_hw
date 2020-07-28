# class Shape:
#     ''' An example class that defines an empty abstract shape '''
#     initiated = False  # 记录shape是否已经被定义为某个形状

#     def get_area(self):
#         ''' virtual method to calculate area of a shape'''
#         pass

#     @classmethod
#     def is_init(cls):
#         ''' return True if a shape has been assigned to the class'''
#         return cls.initiated


# class Square(Shape):
#     ''' A subclass of Shape, specifically for calculating square area'''

#     def __init__(self, width):
#         self.width = width
#         self.get_area()
#         self.__class__.initiated = True

#     def get_area(self):
#         ''' Area of a square is its width times width'''
#         self.area = self.width * self.width
#         return self.area

#     def __add__(self, other):
#         if self.width == other.width:
#             rect = Rectangle(self.width, self.width * 2)
#             return rect
#         else:
#             return None

# class Rectangle(Shape):
#     ''' A subclass of Shape, specifically for calculating rectangle area'''

#     def __init__(self,width,length):
#         self.width = width
#         self.length = length
#         self.get_area()
#         self.__class__.initiated = True

#     def get_area(self):
#         ''' Area of a rectangle is its width times width'''
#         self.area = self.width * self.length
#         return self.area
#EX1.4
class Basketball:

    schedule = []

    def __init__(self, team_number, team_address, team_coach, team_player ):
        self.team_number = int(team_number)
        self.team_address = str(team_address)
        self.team_coach = str(team_coach)
        self.team_player = []
        for i in range(team_number):
            self.team_player.append(i)

    def match_game(self, team_player):
        self.team_player = team_player
        for i in range(len(self.team_player)):
            team = random.randint(1,len(self.team_player) - 1)
            if i != team:
                schedule.append([i,'VS',team])
            else:
                continue
        return schedule