#Author: Yu Qiushuang
#ex1.1 
class Vehicle:
    '''A class to show different kinds of vehicle.'''
    type = {'sedan','convertible','SUV','truck','coupe','van'}
    fuel_level = 0.5
    def __init__(self, brand, model, type):
            self.brand = brand
            self.model = model
            self.type = type
            if self.type not in Vehicle.type:
                print('type', self.type, 'is not existed.')
                self.type = 'sedan'
    
    def __str__(self):
        return 'the brand is {},the model is {},the type of car is {}'.format(self.brand, self.model, self.type)

    def check_fuel_level(self):
        print(self.fuel_level) 

    def set_fuel_level(self,fuel_level):
        if  0 <= fuel_level <= 1:
            self.fuel_level = fuel_level
            return self.fuel_level
        else:
            print('the format of fuel level is wrong, fuel will be set to 0.5')
            self.fuel_level == 0.5


#######################Vehicle calss test start#####################################
volvo = Vehicle('volvo', 'polestar 2', 'sedan')
volvo.set_fuel_level(0.9)
volvo.check_fuel_level()
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
        return 'the team_name is {},the team_address is {},the team_coach  is {},the team_number  is {},the team_player_list is {}'\
            .format(self.team_name, self.team_address, self.team_coach, self.team_number,self.team_player_list)

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
        #league_list[1:] ==> length == 15
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
