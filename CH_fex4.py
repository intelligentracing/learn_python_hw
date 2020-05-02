class Vehicle:
    '''A class to show different kinds of vehicle.'''
    type = {'sedan','convertible','SUV','truck','coupe','van'}

    def __init__(self, brand, model):
            self.brand = str(brand)
            self.model = str(model)
            self.fuel_level = float(0)

    def check_fuel_level(self,fuel_level):
        self.fuel_level = fuel_level
        self.check_fuel_level = self.fuel_level / 100
        return self.check_fuel_level, '%'

    def set_fuel_level(self):
        set_level = input('fuel_level by percentage:')
        self.set_level = set_level
        return self.set_level