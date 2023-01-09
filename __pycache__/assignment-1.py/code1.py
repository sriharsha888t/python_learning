import csv
import pandas as pd
import functools


def csv_reader(option):
    #option = input("What do you want to know:\n 1.Transactions \n 2.Totals \n-->")
    per_month = 2600
    if option == "1":
        flat_num = input("Which flat you want to know the transactions:")
        with open('Transactions.csv',newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
       # print(reader.fieldnames[1:2],end='')
       # print(reader.fieldnames[4:6],end='')
       # print(reader.fieldnames[3],end='')
       # print(reader.fieldnames[2])
            a = reader.fieldnames
       # print(type(a))
            print(a[1],'\t',a[4],'\t\t',a[5],'\t',a[3],'\t\t',a[2])      
            for row in reader:
               if row["Flat#"] == flat_num:
                  print(f"{row['Date']}, {row['Month']}, {row['Flat#']}, {row['Chq./Ref.No.']}, {row['Narration']}")


    elif option == "2":
        column = input("what do you want to know the summary for \n 1. Flat \n 2. Month")
        if column  == "1":
            flat_no = input("Flat No")
            with open('Transactions.csv', newline='') as csvfile:
                 reader = csv.DictReader(csvfile, delimiter=',')
                 for row in reader:
                    if row["Flat#"] == flat_no:
                       paid = row["Deposit Amt."]
                       pending_amount = per_month - float(paid)
                    if pending_amount < 0:
                        print(f"pending amount {pending_amount}")
                    else:
                        print(f"Paid, no pending amount. Balance {pending_amount}")
        if column  == "2":
            month = input("Month")
            with open('Transactions.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                records = 0
                total_paid = 0
                for row in reader:
                     if row["Month"] == month:
                        records += 1
                        total_paid += float(row["Deposit Amt."])
            
            total_pay = records * per_month 
            print(f"total pay {total_pay}")
            print(f"total paid {total_paid}")



option = input("What do you want to know:\n 1.Transactions \n 2.Totals \n-->")
result = csv_reader(option)
print(result)

exit(1)
#dict_file = csv.DictReader(open("Transactions.csv"))



if option == '1':  
    with open("Transactions.csv") as file1:
        csv_reader = csv.reader(file1,delimiter=',') 
        flat_num = input("Which flat you want to know the transactions:")
        flat_details = []
        for col in csv_reader:
            if flat_num in col:
                flat_details.append([col[1],col[4],col[5],col[3],col[2]])
    for i in flat_details:
        print(i)

elif option == '2':
    with open("Transactions.csv") as file2:
        csv_reader2 = csv.DictReader(file2,delimiter=',')
        info = input("What do you want to know the summary for \n 1.Flat \n 2.Month \n-->")
        if info == '1':
            flat = input("Enter the flat number to know deposit and pending:")
            deposit = []
            for i in csv_reader2:
                if flat in i:
                    deposit.append(i)
            
            print(a)
            


        else:
            month = input("Enter the month:")
            month_amount = []
            records = []
            for i in csv_reader2:
                if month in i:
                    records += 1
                    month_amount.append(i[6])

            #print(month_amount)
            a = [int(a) for a in month_amount]
            total_amount = sum(a)
            pending = 200200 - total_amount
            print("The amount paid:",total_amount)
            print("Pending:",pending)




        

            
            
            
             



                    

            