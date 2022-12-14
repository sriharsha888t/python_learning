from abc import ABC,abstractmethod
class Polygon(ABC):
    def sides(self):
       pass

class Triangle(Polygon):
    def sides(self):
        print("Triangle has 3 sides")

class Pentagon(Polygon):
    def sides(self):
        print("Pentagon has 5 sides")

class Hexagon(Polygon):
    def sides(self):
        print("hexagon has 6 sides")

class Square(Polygon):
    def sides(self):
        print("square has 4 sides")


t = Triangle()
t.sides()

p = Pentagon()
p.sides()

h = Hexagon()
h.sides()

s = Square()
s.sides()

p = Polygon()
p.sides()
