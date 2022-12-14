class grandfather:
    def property1(self):
        print("one building")

class father(grandfather):
    def property2(self):
        print("two acres of land")

class son(father):
    def property3(self):
        print("car")

p1 = son()
p1.property1()
p1.property2()
p1.property3()

p2 = father()
p2.property1()
p2.property2()
