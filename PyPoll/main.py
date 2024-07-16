import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_votes = {}

with open(election_data, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

winner = max(candidate_votes, key=candidate_votes.get)

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

print(output_text)

with open("election_results.txt", "w") as text_file:
    text_file.write(output_text)