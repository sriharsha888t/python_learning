# multiple inheritance
class Thar:
    def car(self):
        print("This is a Thar")

class bolero:
    def truck(self):
        print("This is a bolero")

class mahindra(Thar,bolero):    # mahindra is child class for both thar and bolero
    def company(self):
        print("mahindra manufactures cars and trucks")

vehicle = mahindra()
vehicle.car()
vehicle.truck()
vehicle.company()