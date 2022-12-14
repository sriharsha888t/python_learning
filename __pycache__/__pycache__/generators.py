def new(dict):
    for x,y in dict.items():
        yield x,y
a = { 1 : "hi", 2 : "welcome" }
b = new(a)
print(b)  # generator object
print(next(b))  # generator
print(next(b))  # generator
#print(next(b)) stopsIteration