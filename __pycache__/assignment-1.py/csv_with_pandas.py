import csv
import pandas as pd

trans = pd.read_csv("Transactions.csv")

option = input("What do you want to know:\n 1.Transactions \n 2.Totals \n-->")

if option == '1':
    flat_num = input("Which flat you want to know the transactions:")  
    print(trans.loc[trans['Flat#'] == flat_num])
    
    #flat_details =[]
    #  if flat_num in i:
     #     print(trans.loc[trans['Flat#'] == flat_num])
          


elif option == '2':
    summary = input("What do you want to know sammary for \n 1.Flat \n 2.month \n-->")
    if summary == '1':
        flat_number = input("Enter the flat number:")
        deposit = []
        for row in trans:
            if flat_number in row:
                deposit.append(row[6])
        print(deposit)

    

         
     

