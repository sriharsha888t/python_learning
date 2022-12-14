class vehicle:
    color = "blue"
    def __init__(self,company,milage,max_speed,s_capacity):
        self.company = company
        self.milage = milage
        self.max_speed = max_speed
        self.s_capacity =s_capacity
class bus(vehicle):
    def __init__(self):
        pass
class car(vehicle):
    def __init__(self):
        pass

bus = vehicle("vovlo","10kmpl","150kmph","30")
car = vehicle("mahindra","30kmpl","250kmph","5")
print("VEHICLES DETAILS :")
print('\n')
print("company : "+car.company, '\t',"color : "+car.color ,'\t',"max_speed:"+car.max_speed,'\t', "milage : "+car.milage)
print('')
print("company : "+bus.company, '\t',"color :" +bus.color,'\t',"max_speed :"+bus.max_speed,'\t',"milage : "+bus.milage)

