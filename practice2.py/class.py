class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
       
    def info(self):
       print( self.name,self.id)

s = student('harsha',12)
s.info()