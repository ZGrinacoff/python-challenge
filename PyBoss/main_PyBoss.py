import os
import csv

# Import datetime.
from datetime import datetime

pyboss_csv = os.path.join('employee_data.csv')
#print(pyboss_csv)

# State abbreviation dictionary.
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Empty lists to hold row data per column.
emp_id = []
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
        emp_id.append(row[2])

        # Splits column Names into two separate First/Last names lists.
        names = row[1].split(' ')
        First_Name.append(names[0])
        Last_Name.append(names[1])
    #print(First_Name)
    #print(Last_Name)

        # Drops all dates into old date format list to be reformatted with datetime.
        old_date_format = row[2]
        #print(type(old_date_format))
        datetimeobject = datetime.strptime(old_date_format,'%Y-%m-%d')
        new_date_format = datetimeobject.strftime('%m/%d/%Y')
        #print(type(new_date_format))

        # Reformat SSN.
        ssn_old = row[3]
        ssn_new.append('***-**-' + ssn_old.split('-')[2])
        #print(ssn_new)

        


