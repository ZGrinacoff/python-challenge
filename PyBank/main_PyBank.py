import os
import csv

# Path to collect data from PyBank folder.
pybank_csv = os.path.join('budget_data.csv')

# Create empty list to hold dates when file read in.
dates = []
revenue_change_list = []
# Read in the csv file: append dates to lists,
# collect total revvenue, and revenue change stats.
with open(pybank_csv,'r') as csvfile:

    # Split the data on columns.
    csvreader = csv.reader(csvfile,delimiter = ',')

    # Read the header row first.
    header = next(csvreader)
    #print(f"Header: {header}")

    # Add variables to hold total revenue and revenue change stats.
    prev_revenue = 0
    max_rev_inc = 0
    max_rev_dec = 0
    total_revenue_change = 0
    total_revenue = 0
    greatest_month_increase = 0
    greatest_month_decrease = 0

    # Read in csvfile
    for row in csvreader:
        dates.append(row[0]) 
        total_revenue = total_revenue + int(row[1])
        revenue_change = int(row[1]) - prev_revenue
        revenue_change_list.append(revenue_change)
        prev_revenue = int(row[1])

        # Two separate conditionals for max/min changes and respective date.
        if (revenue_change > max_rev_inc):
            max_rev_inc = revenue_change
            greatest_month_increase = row[0]
        
        if (revenue_change < max_rev_dec):
            max_rev_dec = revenue_change
            greatest_month_decrease = row[0]

# Count total months.
total_months = len(dates)
#print(total_months)

# Calculation for average change.
def average(revenue_change_list):
    x = len(revenue_change_list)
    total = sum(revenue_change_list) - revenue_change_list[0]
    avg = total / (x - 1)
    return avg
average_change = round(average(revenue_change_list), 2)

# Print results out to terminal window.
print("Financial Analysis")
print("-"*50)
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${total_revenue: ,d}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_month_increase} ${max_rev_inc: ,d}")
print(f"Greatest Decrease in Profits: {greatest_month_decrease} ${max_rev_dec: ,d}")

# Create path for output file in the same folder.
output_path = os.path.join("output_main_PyBank.txt")

# Opens .txt file in write mode and writes summary.
with open(output_path, 'w') as writefile:
    writefile.writelines("Financial Analysis\n")
    writefile.writelines("-"*50)
    writefile.writelines(f"\nTotal Months: {total_months}\n")
    writefile.writelines(f"Total Revenue: ${total_revenue: ,d}\n")
    writefile.writelines(f"Average Change: $ {average_change}\n")
    writefile.writelines(f"Greatest Increase in Profits: {greatest_month_increase} ${max_rev_inc: ,d}\n")
    writefile.writelines(f"Greatest Decrease in Profits: {greatest_month_decrease} (${max_rev_dec: ,d})\n")

