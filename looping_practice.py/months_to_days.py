# january,march,may,july,august,october,december = 31
# april,june,september,november = 30
# february = 28

#month = list(input("Enter the month:"))
days_31 = ['january','march','may','july','august','october','december']

days_30 = ['april','june','september','november']

month = ['january','march','may','july','august','october','december','april','june','september','november','february ']
choice = input("enter the month:")
for i in month:
    if i == "febraury" and choice == "febraury":
        print("febraury has 28 or 29 days.")
        
    elif i in days_31  and choice in days_31:
        print("month has 31 days.")
        
    elif i in days_30 and choice in days_30:
        print("month has 30 days")
        
    else:
        print("Invalid input.")
        break
        
        


