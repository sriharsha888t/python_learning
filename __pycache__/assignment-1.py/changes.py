import csv
import pandas as pd

#dict_file = csv.DictReader(open("Transactions.csv"))

option = input("What do you want to know:\n 1.Transactions \n 2.Totals \n-->")


if option == '1':  
    with open("Transactions.csv") as file1:
        csv_reader = csv.reader(file1,delimiter=',') 
        flat_num = input("Which flat you want to know the transactions:")
        flat_details = []
        for row in csv_reader:
            if flat_num in row:               
                flat_details.append([row[4],row[5],row[3],row[2]])
        
   
   # print(flat_details)
   # for i in flat_details:
     #   print(i)
elif option == '2':
    with open("Transactions.csv") as file2:
        csv_reader2 =csv.reader(file2,delimiter=',')
        d = input("which month")
        for i in d:
            if i[6] == d:
                print(i[-1])