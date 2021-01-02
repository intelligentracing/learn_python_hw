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
            
class ElectricVehicle(Vehicle):

    def __init__(self, brand, model,type, charge_level):
        super().__init__(brand,model,type)
        if  0 <= charge_level <= 1:
            self.charge_level = charge_level
        else:
            print('the charge level should be smaller than 1!')

    def check_fuel_level(self,fuel_level):
        print('check_fuel_level is unavilable')

    def set_fuel_level(self):
        print('set_fuel_level is unavilable.')

    def check_charge_level(self,charge_level):
        self.charge_level = charge_level
        return self.charge_level

    def set_charge_level(self):
        self.charge_level = input('charge_level by percentage:')
        return 'the charge level has been update:{}%'.format(self.charge_level)

########################### test Vehicle & ElectricVehicle class #####################################
M4 = Vehicle('BMV','M4','van')
print(M4.check_fuel_level(0.5))
print(M4.set_fuel_level(1))

car = ElectricVehicle('Porsche','cayenne','SUV',0.1)
print(car)
car.check_fuel_level(0.5)
print(car.set_charge_level())