# cheching the object belongs to which class
class vehicle:
    def __init__(self,milage,maxspeed,model):
        self.milage = milage
        self.maxspeed = maxspeed
        self.model = model
class bus(vehicle):
    pass

b = bus("10kmpl","120kmph","volvo")
print(b.model,b.milage,b.maxspeed)
v = vehicle(12,10,123)

print(type(b))
print(type(v))

# checking bus is an instance of vehicle
print(isinstance(bus,vehicle))
print(issubclass(bus,vehicle))
