import os
import csv

# Path to collect data from PyBank folder.
pybank_csv = os.path.join('budget_data.csv')

# Create empty lists to hold column(s) data.
dates = []
revenue = []

# Read in the csv file and append data to lists.
with open(pybank_csv,'r') as csvfile:

    # Split the data on columns.
    csvreader = csv.reader(csvfile,delimiter = ',')

    # Read the header row first.
    header = next(csvreader)
    #print(f"Header: {header}")

    for row in csvreader:
        dates.append(row[0])
        revenue.append(int(row[1]))
        #print(dates)

# Count total months.
total_months = len(dates)
#print(total_months)
# Correctly counted number of distinct months.

# Create variables to hold greatest increase/decrease.
# Set them equal to the first row/entry in list.
# Then add each revenue to total revenue.
greatest_increase = revenue[0]
greatest_decrease = revenue[0]
total_revenue = 0







