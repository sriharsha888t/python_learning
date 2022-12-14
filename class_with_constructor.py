class car():
    def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price
def price_inc(self):
    self.price=(self.price*1.05)



honda=car('city',2020,1000000)
tata=car("harrier",2021,1500000)

honda.cc=1500

print(tata.__dict__)
print(honda.__dict__)

tata.cc=1200
print(tata.__dict__)