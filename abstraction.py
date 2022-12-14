# implimentation of abstraction class
from abc import ABC,abstractmethod

class Car(ABC):
    def milage(self):
        pass

class tesla(Car):
    def milage(self):
        print("milage is 30kmpl")

class suzuki(Car):
    def milage(self):
        print("milage is 25kmpl")

class mahindra(Car):
    def milage(self):
        print("milage is 20kmpl")


t = tesla()
t.milage()


s = suzuki()
s.milage()

m = mahindra()
m.milage()
