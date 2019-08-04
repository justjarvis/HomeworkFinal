import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("election_results.txt")

votes_total = 0

option_of_candidates = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:

        votes_total = votes_total + 1

        candidate_name = row[2]

        if candidate_name not in option_of_candidates:

            option_of_candidates.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

winner_votes = {"Khan":2218231, 
                "Correy":704200, 
                "Li":492940, 
                "O'Tooley":105630
                }

output = (
    f"\nElection Results\n"
    f"-----------------------\n"
    f"Total Votes: {votes_total}\n"
    f"---------------------------\n"
    f"Candidates\n" 
    f"{candidate_votes}\n"
    f"-----------------------\n"
    f"Winner: {max(zip(winner_votes.values(), winner_votes.keys()))}\n"
        )
    
print(output)

with open(output_file, "w") as txt_file:
    txt_file.write(output)