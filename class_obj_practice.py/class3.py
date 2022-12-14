# bus(derived class) aquiring the proprties of vehicle  (base class)
class vehicle:
    def __init__(self,milage,maxspeed,model):
        self.milage = milage
        self.maxspeed = maxspeed
        self.model = model
class bus(vehicle):
    pass

b = bus("10kmpl","120kmph","volvo")
print(b.model,b.milage,b.maxspeed)