import os
import csv

# Import datetime.
from datetime import datetime

pyboss_csv = os.path.join('employee_data.csv')
#print(pyboss_csv)

# Empty lists to hold row data per column.
Emp_ID = []
names = []
First_Name = []
Last_Name = []
old_date_format = []
new_date_format = []
ssn_old = []
ssn_new = []

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

        # Drops all dates into old date format list to be reformatted with datetime.
        old_date_format = row[2]
        #print(old_date_format)
        datetimeobject = datetime.strptime(old_date_format,'%Y-%m-%d')
        new_date_format = datetimeobject.strftime('%m/%d/%Y')
        #print(new_date_format)

        # Reformat SSN.
        ssn_old = row[3]
        #print(type(ssn_old))
        ssn_new = ssn_old.


