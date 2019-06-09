import os
import csv

pyboss_csv = os.path.join('employee_data.csv')
#print(pyboss_csv)

# Empty lists to hold row data per column.
Emp_ID = []
names = []
First_Name = []
Last_Name = []

# Read in csv file.
with open(pyboss_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    for row in csvreader:
        
        # Drops all employee ids into new list.
        Emp_ID = row[0]

        # Splits column Names into two separate First/Last names lists.
        names = row[1].split(' ')
        First_Name.append(names[0])
        Last_Name.append(names[1])
    #print(First_Name)
    #print(Last_Name)