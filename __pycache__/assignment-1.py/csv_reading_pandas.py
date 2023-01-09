import csv
import pandas as pd

df = pd.read_csv("Transactions.csv")
#print(df.head())

#print(df.loc[0:1,])
#print(df.loc[0:3 ,['Deposit Amt.','Reciept']])
#print(df.loc[1:4],)
#print(df.loc[df['Flat#'] == 'A402'])
print(df.loc[:],)