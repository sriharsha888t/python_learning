amt = 0
nu = int(input("enter total units:"))
if nu <= 100:
    amt = 0
elif nu > 100:
    amt = (nu - 100) * 5
else:
    amt = 500 + (nu - 200) * 10
print("amount to pay:",amt)