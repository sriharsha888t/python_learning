# adding a default argument in child class
class vehicle:
    def __init__(self,name,milage,max_speed):
        self.name = name
        self.milage = milage
        self.max_speed = max_speed
class bus(vehicle):
    def details(self,capacity = 20):
        self.capacity = capacity
b = bus("volvo","10kmpl","120kmph")
b.details()
print(b.name,b.milage,b.max_speed,b.capacity)
