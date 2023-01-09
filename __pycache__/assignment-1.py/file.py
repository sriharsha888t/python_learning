import csv
with open('Transactions.csv') as file:
    readcsv = csv.reader(file)
    
    flats = []
    months = []
    year = []
    date = []
    cheq_ref = []
    narration = []
    deposit_amount = []
    reciepts = []


    for row in readcsv:
        f = row[5]
        m = row[4]
        y = row[0]
        c = row[3]
        dp = row[6]
        r = row[7]
        n = row[2]
        d = row[1]

        flats.append(f)
        months.append(m)
        year.append(y)
        cheq_ref.append(c)
        reciepts.append(r)
        deposit_amount.append(dp)
        narration.append(n)
        date.append(d)
        
class flat:
    def person_details():
       with open("Transactions.csv") as csv__file:
         #  details = input("Enter the flat number to know person details:")
           rows = []
           month = []   
           for row in csv__file:
             # if details in row:
               rows.append(row)
       return rows

#class transaction_month:
#    def total_transactions():
with open("Transactions.csv") as csv_file:
    mon = input("Enter the month to print total transactions:")
    month_transactions = []
    for row in csv_file:
        if mon in row:
            month_transactions.append(row)
    print(month_transactions)

    
            
        
   
   
    



