option = input("What do you want to know \n 1.Transactions \n 2.Totals \n:")
if option == '1':
    with open("Transactions.csv") as csv__file:
        flat_num = input("Which flat you want to know the transactions:")
        rows = []  
        for row in csv__file:
           if flat_num in row:
              rows.append(row)       
    print(rows)
elif option == '2':
    with open("Transactions.csv") as csv__file:
        summary = input("What do you want to know summary for \n 1.Flat \n 2.Month \n:")
        if summary == '1':
            flat_number = input("Enter flat number to know total amount paid and pending:")
            amount_paid = []
            pending_amount = []
            for row in csv__file:
                if flat_number in csv__file:
                    amount_paid.append(row)
    print(amount_paid)
                    




