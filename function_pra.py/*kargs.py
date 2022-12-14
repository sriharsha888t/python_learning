# function with **kwargs
def function(**kargs_list):
    a = []
    for key,value in kargs_list.items():
        a.append([key,value])
        return a
o = function(first="welcome",second="python",third="programming")
print(o)

def info(**data):
    print("type of argument",type(data))

    for key,value in data.items():
        print("{} is {}".format(key,value))

info(name = "harsha",age = 20,mobile = 1234567890)
info(name = 'kumar',age = 21,mobile = 9876543210)
