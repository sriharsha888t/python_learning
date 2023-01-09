import csv
file = open("Transactions.csv")
type(file)
csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

#row = []
#for row in csvreader:
#    row.append(row)
#print(row,end=' ')
#print()
#flat_num = input("Enter which plat number:")
col = []
with open('Transactions.csv') as f:
    csv_reader = csv.reader(f) 
    rows = list(csv_reader)
print(rows[1])

e =[]
with open('Transactions.csv') as csv_file:
    a = csv_file.readline(2)
    print(a)



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
        

with open("Transactions.csv") as csv__file:
    details = input("Enter the falt number to know person details:")

    #file = csv.reader(csv__file)
    a = csv__file.readlines(1,2)
    print(a)
       
    




        