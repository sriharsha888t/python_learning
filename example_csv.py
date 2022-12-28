import csv
with open("machine.csv","r") as file:
    machine = csv.reader(file)

print(machine)

   