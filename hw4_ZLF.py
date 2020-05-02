'''定义了一个汽车类，拥有三个变量（brand，model，type），两个方法（set_fuel_level,check_fuel_level）。
电动车为其子类'''

class Vehicle():
    def __init__(self,brand,model,Type):###初始方法，有三个变量
        self.brand = brand
        self.model = model
        self.Type = Type

    def set_fuel_level(self,fuel_level):###添加一个油的变量
        self.fuel_level = fuel_level

    def check_fuel_level(self):###检查油
        print(self.fuel_level)

class ElectricVehicle(Vehicle):

    def set_fuel_level(self,fuel_level):###对父类方法进行复写
        print('electric vehicle does not use fuel')

    def check_fuel_level(self):###对父类复写
        print('electric vehicle does not use fuel')

    def set_charge_level(self,charge_level):###子类专属方法
        self.charge_level = charge_level

    def check_charge_level(self):###子类专属方法
        print(self.charge_level)

ElectricVehicle('smart','unknown',{'sudan','convertible'})###测试
