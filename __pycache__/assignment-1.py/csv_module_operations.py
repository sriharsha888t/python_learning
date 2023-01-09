import csv

with open("Transactions.csv") as f:
    df = csv.DictReader(f)
    print(df.dialect())