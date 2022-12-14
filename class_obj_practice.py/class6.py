class vehicle:
    color = "blue"
    def __init__(self,company,milage,max_speed,s_capacity):
        self.company = company
        self.milage = milage
        self.max_speed = max_speed
        self.s_capacity =s_capacity

    def fare(self):
        return self.s_capacity * 100

class bus(vehicle):
     def fare(self):
            amount = super().fare()
            amount += amount * 10 / 100
            return amount

class car(vehicle):
    pass



bus = vehicle("vovlo","10kmpl","150kmph",30)
car = vehicle("mahindra","30kmpl","250kmph","5")
print(bus.color,bus.milage,bus.max_speed ,bus.s_capacity,bus.fare())