# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:05:52 2020

@author: Colin
"""

# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Create a list of county options.
county_options = []

# Create a dictionary where key: county and value: number of votes cast.
county_votes = {}

# Create an empty string that will hold the county name that had the largest turnout.
county_highest = ""

# Declare a variable that represents the number of votes that a county received. 
county_total_votes = 0

# Create variables for the highest turnout county and its stats.
highest_county = ""
highest_county_votes = 0
highest_county_percentage = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Hint: Inside a for loop, add an if statement to check if the county name has already been recorded.
        # If not, add it to the list of county names.
        county_name = row[1]
        
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)

            # 2. Begin tracking that county's vote count. 
            county_votes[county_name] = 0
        
        # Add a vote to that county's count.
        county_votes[county_name] += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    # Write the header to the county votes tally.
    county_header = "\nCounty Votes:\n"
    
    print(county_header)
    txt_file.write(county_header)
    
    # Iterate through the counties to write their names and vote counts to the text file.
    for county in county_votes:
        # Retrieve vote count of a county.
        votes = county_votes[county]
        
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        
        # Format a string to write to the file.
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        
        print(county_results)
        
        #  Save the county results to our text file.
        txt_file.write(county_results)

        # Determine highest turnout county
        # Determine if the votes are greater than the highest turnout.
        if (votes > highest_county_votes) and (vote_percentage > highest_county_percentage):
            # If true then set highest_county_votes = votes and highest_county_percentage = vote_percentage.
            highest_county_votes = votes
            highest_county_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            highest_county = county
            
    highest_county_summary = (f"\n-------------------------\n"
                              f"Largest County Turnout: {highest_county}\n"
                              f"-------------------------\n")
    
    print(highest_county_summary)

    # Save the highest turnout county's name to the text file.
    txt_file.write(highest_county_summary)
    
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        
        #  To do: print out the winning candidate, vote count and percentage to terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate  
        
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
