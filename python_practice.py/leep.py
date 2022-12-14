import calendar
def is_leep(year):
    leep = False
    if calendar.isleap(year):
      leep = True
      print("leep year")
    else:
        leep = False
        print("not a leep")
    return leep


year = int(input("enter year:"))
is_leep(year)


