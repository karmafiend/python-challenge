#PyPoll scripting file-Chris Kilkes

#PyPoll module instructions:
#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
#You will be given a set of poll data called election_data.csv. 
#The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
#Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Outline the coding:

import os
import csv
from collections import Counter

#Create and include path to CSV

csv_filename = 'election_data.csv'
csv_path = os.path.join(os.path.dirname(__file__), 'Resources', csv_filename)

#Initialize variables

#votes_won_percentage = 0
total_votes = 0
candidate_votes = {}
winner = None
winner_votes = 0
candidate = None

#Read the CSV file

with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip the header row

#Loop through each row in the CSV
    
    for row in csvreader:
        total_votes += 1
        candidate = row[2] #candidate name/vote is in column C or index column 2
    #Count the votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

#Determine the winner
for candidate, votes in candidate_votes.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

#Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

#Print the analysis to the terminal

print("Election Results")
print("----------------")
print(f"Total Votes: {total_votes}")
print("-----------------")        
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}%({votes})")                                            
print("------------------")
print(f"Winner: {winner}")
print("------------------")

#Export the results to a text file
                                                                          
output_filename = "election_results.txt"
analysis_folder = os.path.join(os.path.dirname(__file__), 'analysis')
output_file_path = os.path.join(analysis_folder, output_filename)

with open(output_file_path, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        textfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")

print(f"Results have been exported to '{output_file_path}'") 
