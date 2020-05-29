# A CLASS AND A SUBCLASS
# Design in Python a class named Vehicle. A Vehicle class should contain the 
# following attributes:
# • brand: string type
# • model: string type
# • type: set type {‘sedan’, ’convertible’, ‘SUV’, ‘truck’, ‘coupe’, ‘van’} 
# • fuel_level: float type in percentage
# Among the four attributes, the first three should be initiated when an 
# object is created. For the last attribute, design a check_fuel_level() 
# method to print the fuel_level value, and design a set_fuel_level() 
# method to set the fuel_level value.
# Further, design a subclass of Vehicle, named ElectricVehicle. In this 
# subclass, add an additional attribute:
# • charge_level: float type in percentage.
# Since an electric vehicle does not use fuel, the check_fuel_level() 
# and set_fuel_level() methods need to be overwritten to disable reading 
# or setting the fuel_level attribute, and print messages to inform the 
# user. Finally, add two new methods: check_charge_level() and set_charge_level(), 
# which will print out or set the charge_level value, respectively.


class Car:
    ''' An example class that defines an empty abstract shape '''
    initiated = False

    @classmethod
    def is_init(cls):
        ''' return True if a shape has been assigned to the class'''
        return cls.initiated

class Vehicle(Car):

    def __init__(self, brand,model,typ):
        carset=set(["sedan", "convertible", "SUV", "truck", "coupe", "van"])
        self.brand = brand
        self.model = model
        self.type = set(typ)
        self.fuel=0.0   
        self.__class__.initiated = True     
    
    def check_fuel_level(self):
        print(self.fuel)

    def set_fuel_level(self, fuel):
        self.fuel=fuel

class ElectricVehicle(Vehicle):

    def __init__(self, brand,model,typ):
        super().__init__(brand,model,typ)
        del self.fuel
        self.charge_level=0.0
        self.__class__.initiated = True    
    
    def check_fuel_level(self):
        pass

    def set_fuel_level(self,fuel):
        pass

    def check_charge_level(self):
        print(self.charge_level)

    def set_charge_level(self, charge):
        self.charge_level=charge
