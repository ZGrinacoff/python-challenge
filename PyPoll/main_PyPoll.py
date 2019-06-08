import os
import csv

pypoll_csv = os.path.join('PyPoll', 'election_data.csv')

# Create dictionary for polling candidate's name and vote count.
# To be read in when csv is opened.
#poll_data = {}

# Create variable for total vote count and set to 0.
#total_vote = 0

# Read in the csv file.
with open(pypoll_csv,'r') as csvfile:

    # Split the data on columns.
    csvreader = csv.reader(csvfile,delimiter = ',')

    # Read the header row first.
    header = next(csvreader)
    print(f"Header: {header}")