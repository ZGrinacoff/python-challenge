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
    vote_percent.append(round(num/total_vote*100, 1))
#print(vote_percent)

# Zip candidate, number of votes, and vote percent into tuples in list.
# To be used for winner check.
clean_candidate_data = list(zip(candidate, number_of_votes, vote_percent))
#print(clean_candidate_data)

# Create an empty list for winner.
winner = []
# Loop through all of the individual candidate data to determine winner by pop vote.
for candidate in clean_candidate_data:
    if max(number_of_votes) == candidate[1]:
    #print(candidate[1])
        winner.append(candidate[0])
    #print(winner[0])

# Create list for winning candidate by indexing only one item in list.
win = winner[0]
#print(win)

# Print results out to terminal window.
print("Election Results")
print("-"*26)
print(f"Total Votes: {total_vote: ,d}")
print("-"*26)
# Loop through clean candidate data to return candidate summary.
# Added 2 extra zeros to end of vote percent.
for output in clean_candidate_data:
    print(f"{output[0]}: {output[2]}00% ({output[1]:,d})")
print("-"*26)
print(f"Winner: {win}")
print("-"*26)

# Create path for output file in the same folder.
output_path = os.path.join("output_main_PyPoll.txt")

# Opens .txt file in write mode and writes summary.
with open(output_path, 'w') as writefile:
    writefile.writelines("Election Results\n")
    writefile.writelines("-"*26)
    writefile.writelines(f"\nTotal Votes: {total_vote: ,d}\n")
    writefile.writelines("-"*26)
    # Loop through clean candidate data to return candidate summary.
    # Added 2 extra zeros to end of vote percent.
    for output in clean_candidate_data:
        writefile.writelines(f"\n{output[0]}: {output[2]}00% ({output[1]:,d})")
    writefile.writelines("\n")
    writefile.writelines("-"*26)
    writefile.writelines(f"\nWinner: {win}\n")
    writefile.writelines("-"*26)