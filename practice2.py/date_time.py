import datetime
today = datetime.datetime.now()
print(today.strftime("%y-%m-%d ,%H:%M:%S"))

a = datetime.datetime.date(today)
print(a)

b = datetime.datetime.time(today)
print(b)
