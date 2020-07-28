class Vehicle:
    '''A class to show different kinds of vehicle.'''
    type = {'sedan','convertible','SUV','truck','coupe','van'}

    def __init__(self, brand, model):
            self.brand = str(brand)
            self.model = str(model)
            self.fuel_level = None
            if self.type not in type:
                print('type', self.type, 'is not existed.')
                self.type = 'sedan'
    def check_fuel_level(self,fuel_level):
        self.fuel_level = fuel_level
        return self.fuel_level

    def set_fuel_level(self,fuel_level):
        if  0 <= fuel_level <= 1:
            self.fuel_level = fuel_level
            return self.set_level
        else:
            print('the format of fuel level is wrong, fuel will be set to 0.5')
            return self.fuel_level = 0.5
            
class ElectricVehicle(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand,model)
        self.charge_level = float(0)


    def check_fuel_level(self,fuel_level):
        super().check_fuel_level()
        print('check_fuel_level is unavilable')

    def set_fuel_level(self):
        super().set_fuel_level()
        print('set_fuel_level is unavilable.')

    def check_charge_level(self,charge_level):
        self.charge_level = charge_level
        self.check_level = self.charge_level / 100
        return self.check_level, '%'

     def set_charge_level(self):
         set_level = input('charge_level by percentage:')
         self.set_level = set_level
         return self.set_level