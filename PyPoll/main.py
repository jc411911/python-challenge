import os
import csv

# Path to the CSV file
election_data = os.path.join("Resources", "election_data.csv")

# Setting variables
total_votes = 0
candidate_votes = {}

# Open the CSV file and read its content
with open(election_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        total_votes += 1  
        candidate = row[2]  # Get the candidate's name from the row
        
        # If the candidate is not already in dictionary add
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1  # Increment the candidate's vote count

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Prepare the output 
output = []
output.append("Election Results")
output.append("-------------------------")
output.append(f"Total Votes: {total_votes}")
output.append("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    output.append(f"{candidate}: {percentage:.3f}% ({votes})")
output.append("-------------------------")
output.append(f"Winner: {winner}")
output.append("-------------------------")


output_text = "\n".join(output)

# Print the output to the terminal
print(output_text)

# Write the output to a text file
with open("election_results.txt", "w") as text_file:
    text_file.write(output_text)
