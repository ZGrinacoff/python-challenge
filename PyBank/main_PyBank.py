import os
import csv

# Path to collect data from PyBank folder.
pybank_csv = os.path.join('budget_data.csv')

# Create empty lists to hold column(s) data.
dates = []
revenue = []

# Read in the csv file.
with open(pybank_csv,'r') as csvfile:

    # Split the data on columns.
    csvreader = csv.reader(csvfile,delimiter = ',')

    # Read the header row first.
    header = next(csvreader)
    #print(f"Header: {header}")





