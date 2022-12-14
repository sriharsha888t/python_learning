class Animal:
    def speaks(self):
        print("animal speaks:")

class dog(Animal):
    def barks(self):
        print("dog barking")

d = dog()
d.speaks()
d.barks()


class car:
    def properties(self):
        print("car properties::")
        print("one steering")
        print("four wheels")
        print("two doors")

class thar(car):
    def property():
        print("this is thar") 

mycar = thar()
mycar.properties()