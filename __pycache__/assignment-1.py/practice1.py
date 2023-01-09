import csv

with open("Transactions.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader)
    date = input("Enter the date to know the transactions:")
    a = []
    for row in reader:
        if row["Date"] == date:
          print(f" {row['Flat#']},{row['Deposit Amt.']}")
  
  