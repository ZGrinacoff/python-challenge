import os
import csv

pypoll_csv = os.path.join('election_data.csv')

# Create dictionary for polling candidate's name and vote count.
# To be read in when csv is opened.
poll_data = {}

# Create variable for total vote count and set to 0.
total_vote = 0

# Read in the csv file.
with open(pypoll_csv,'r') as csvfile:

    # Split the data on columns.
    csvreader = csv.reader(csvfile,delimiter = ',')

    # Read the header row first.
    header = next(csvreader)
    #print(f"Header: {header}")

    # Read csv into poll_data dictionary for each candidate
    # and their individual vote count.
    for row in csvreader:

        # Add to the total vote couunt for each interation.
        total_vote += 1

        # Adds 1 to count if name already found in dict.
        # Set count to one for each new name.
        if row[2] in poll_data.keys():
            poll_data[row[2]] += 1
        else:
            poll_data[row[2]] = 1

# Create empty lists to store candidate name an their respective share of the votes.
candidate = []
number_of_votes = []

# Loop through poll data dictionary and store key:candidate/value:number_of_votes in lists.
for key, value in poll_data.items():
    candidate.append(key)
    number_of_votes.append(value)

#print(candidate)
#print(number_of_votes)

# Create empty list to hold vote percent.
vote_percent = []

# Loop through number of votes and perform percent calculation for each candidate.
for num in number_of_votes:
    vote_percent.append(round(num/total_vote*100))
#print(vote_percent)    