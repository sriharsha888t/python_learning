import csv

#dict_file = csv.DictReader(open("Transactions.csv"))

option = input("What do you want to know:\n 1.Transactions \n 2.Totals \n-->")


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
    print()
    
   
    

elif option == '2':
    with open("Transactions.csv") as file2:
        csv_reader2 = csv.reader(file2,delimiter=',')
        info = input("What do you want to know the summary for \n 1.Flat \n 2.Month \n-->")
        if info == '1':
            flat = input("Enter the flat number to know deposit and pending:")
            deposit = []
            receipt = []
            for col in csv_reader2:
                if flat in col:
                    deposit.append(col[6])    
                    receipt.append(col[7])               
        #print(deposit)
        #print(receipt)
            total_deposit = [int(total_deposit) for total_deposit in deposit]
            total_receipt = [(total_receipt) for total_receipt in receipt]
            sum_of_receipt = sum(total_receipt)
            Total_paid = sum(total_deposit)

            print("The total amount paid:",Total_paid)
            print("The pending amount:",sum_of_receipt - Total_paid)
        
        else:          
            month = input("Enter the month to know deposit and pending:")
            month_deposits = []
            month_receipts = []
            for col in csv_reader2:
                if month in col:
                        month_deposits.append(col[6])
                        month_receipts.append(col[7])
            print("Deposits in month:")
            print(month_deposits)
            print("Pendings in month:")
            print(month_receipts)
            total_depo = [int(total_depo) for total_depo in month_deposits]
            receipt_total = [str(receipt_total) for receipt_total in month_receipts]
            int(receipt_total)
            m_total_amt = sum(total_depo)
            m_recipt_amt = sum(receipt_total)

            print("The Total amount paid:",m_total_amt)
            print("Pending:",m_recipt_amt - m_total_amt)

else:
    print("Invalid Input.")





        




