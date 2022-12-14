# range(stop)
# range(start,stop)
# range(start,stop,step)
for i in range(3):  # one argument by default stop
    print(i)

for i in range(0,3):  # two arguments,that are start and stop
    print(i)

for i in range(5,-5,-1):
    print(i,end=" ")

for i in reversed(range(0,5)):
    print(i)