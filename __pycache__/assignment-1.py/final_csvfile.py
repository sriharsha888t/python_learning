import csv

option = input("What do you want to know:\n 1.Transactions \n 2.Totals \n-->")
per_month = 2600

if option == "1":
    flat_num = input("Which flat you want to know the transactions:")
    with open('Transactions.csv',newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row["Flat#"] == flat_num:
                print(f"{row['Date']}, {row['Month']}, {row['Flat#']}, {row['Chq./Ref.No.']}, {row['Narration']}")

elif option == "2":
    column = input("What do you want to know the summary for \n 1.Flat \n 2.Month \n -->")
    if column  == "1":
        flat_num = input("Enter flat number:")
        per_month = 2600
        with open('Transactions.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                if row["Flat#"] == flat_num:
                    paid = row["Deposit Amt."]
                    pending_amount = per_month - float(paid)              
            print(f"The total amount paid:{paid}")
            if pending_amount < 0:
                print(f"No pending amount. Balance :{pending_amount}")
            else: 
                print(f"pending amount: {pending_amount}")
    if column  == "2":
        month = input("Enter the month:")
        with open('Transactions.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            records = 0
            total_paid = 0
            for row in reader:
                if row["Month"] == month:
                    records += 1
                    total_paid += float(row["Deposit Amt."])
            
            total_pay = records * per_month 
            print(f"Total pay:{total_pay}")
            print(f"The total amount paid:{total_paid}")
            total_pending = total_paid - total_pay
            if total_paid < 0:
                print(f"pending amount:{total_pending}")
            else:
                print(f"No pending amount.balance:{total_pending}")
           # print(total_pending)
           # print(f"total pay {total_pay}")
          #  print(f"total paid {total_paid}")




