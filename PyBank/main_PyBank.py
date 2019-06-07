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

# Loop through all values in revenue list to find greatest increase and decrease.
for rev in range(len(revenue)):
    if revenue[rev] >= greatest_increase:
        greatest_increase = revenue[rev]
        
        # Set date where greatest total revenue is found in list.
        greatest_month_increase = dates[rev]

    elif revenue[rev] <= greatest_decrease:
        greatest_decrease = revenue[rev]
        
        # Set date where greatest total loss is found in list.
        greatest_month_decrease = dates[rev]

    # Add each revenue to calculate total revenue.
    total_revenue += revenue[rev]

# Calculation for average change.
average_change = round(total_revenue/total_months, 2)

# Print results out to terminal window.
print("Financial Analysis")
print("-"*50)
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue: ,d}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_month_increase} ${greatest_increase: ,d}")
print(f"Greatest Decrease in Profits: {greatest_month_decrease} (${greatest_decrease: ,d})")


