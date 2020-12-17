#Author: Yu Qiushuang
#ex1.1 
class Vehicle:
    '''A class to show different kinds of vehicle.'''
    type = {'sedan','convertible','SUV','truck','coupe','van'}

    def __init__(self, brand, model, type):
            self.brand = brand
            self.model = model
            self.type = type
            if self.type not in Vehicle.type:
                print('type', self.type, 'is not existed.')
                self.type = 'sedan'
    
    def __str__(self):
        return 'the brand is {},the model is {},the type of car is {}'.format(self.brand, self.model, self.type)

    def check_fuel_level(self,fuel_level):
        self.fuel_level = fuel_level
        return self.fuel_level

    def set_fuel_level(self,fuel_level):
        if  0 <= fuel_level <= 1:
            self.fuel_level = fuel_level
            return self.fuel_level
        else:
            print('the format of fuel level is wrong, fuel will be set to 0.5')
            self.fuel_level == 0.5


#######################Vehicle calss test start#####################################
# volvo = vehicle('volvo', 'polestar 2', 'sedan')
# volvo.set_fuel_level(0.9)
# volvo.check_fuel_level()
# #######################Vehicle class test end#######################################

#ex1.2
class Basketball:
    def __init__(self, team_name=None, team_address=None, team_coach=None, team_number=None, team_player_list = []):
        self.team_number = team_number
        self.team_address = team_address
        self.team_coach = team_coach
        self.team_name = team_name
        self.team_player_list = team_player_list
        self.schedule = []

    def __str__(self):
        return self.team_name

    def get_team_name(self):
        return self.team_name

    def get_team_address(self):
        return self.team_address

    def get_team_coach(self):
        return self.team_coach

    def get_team_number(self):
        return self.team_number

    def set_team_name(self, s):
        self.team_name = s
        print("team name modified")

    def set_team_address(self, s):
        self.team_address = s
        print("team address modified")

    def set_team_coach(self, s):
        self.team_coach = s
        print("team coach modified")

    def set_team_number(self, lis):
        self.team_number = lis
        print("team member modified")

    def add_team_player_list(self, s):
        self.team_player_list.append(s)
        print("add a team member")

    def generate_game(self, component):
        for i in component:
            self.schedule.append((self.team_name, i.team_name))
            self.schedule.append((i.team_name, self.team_name))
        print("new games add to schedule")

    def get_schedule(self):
        return self.schedule

# #######################basketball class test start##################################
import random
import string
s = string.ascii_uppercase
league_list = []
for i in range(16):
    team_name = random.choice(s)
    team_name += random.choice(s)
    league_list.append(Basketball(team_name))

print(league_list[0])

league_list[0].generate_game(league_list[1:])
print(league_list[0].get_schedule())
#######################basketball calss test end#####################################




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
#ex1.1
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
#######################Rectangle calss test start###################################
# s = Rectangle(6,8)

# print(s.is_init())
# print(s.get_area())
#######################Rectangle class test end######################################


#######################Square class test end######################################
s1 = Square(8)
s2 = Square(8)

enroll = s1 + s2
print(s1.get_area())
print(enroll.get_area())
#######################Square class test end######################################



#EX1.2
# class Basketball:

#     schedule = []

#     def __init__(self, team_name, team_address, team_coach, team_member ):
#         self.team_name = str(team_number)
#         self.team_address = str(team_address)
#         self.team_coach = str(team_coach)
#         self.team_member = []
#         for i in range(team_number):
#             self.team_player.append(i)

#     def match_game(self, team_player):
#         self.team_player = team_player
#         for i in range(len(self.team_player)):
#             team = random.randint(1,len(self.team_player) - 1)
#             if i != team:
#                 schedule.append([i,'VS',team])
#             else:
#                 continue
#         return schedule

