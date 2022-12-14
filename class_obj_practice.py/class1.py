# class with instance attributes
class vehicle:
    def __init__(self,milage,maxspeed):
        self.milage = milage
        self.maxspeed = maxspeed
        print("milage and maximum speed of the vehicle is:" ,self.milage,self.maxspeed)

v1 = vehicle("20kmpl","200kmph")

