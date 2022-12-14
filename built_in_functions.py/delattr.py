class Student:
    id = 100
    name ='harsha'
    mailid='abc@mail'

    def info(self):
        print(self.id,self.name,self.mailid)

s = Student()
s.info()

delattr(info,'mailid')


