import os
import csv


INPUT_CSV_PATH = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidates_list = []
candidate_votes_dict = {}
winner = ""
winning_votes = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0


os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(INPUT_CSV_PATH, 'r') as input_file:
    
    csv_reader = csv.reader(input_file)
    header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidates_list:
            candidates_list.append(candidate)
            candidate_votes_dict[candidate] = 0
        candidate_votes_dict[candidate] += 1
           
print(f"Total_votes: {total_votes}")


for candidate in candidate_votes_dict:

       
    votes = candidate_votes_dict[candidate]
            
    vote_percentage = float(votes)/float(total_votes)*100
                
    candidate_results = (f"{candidate}: {vote_percentage:.1f}%  ({votes:,})\n")
        
    print(candidate_results)

if (votes>winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_candidate equal to the candidate's name
            winning_candidate = candidate
        
        # Print out each candidate's name, vote count and percentage of votes to the terminal.

    
winning_candidate_summary =(
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
print(winning_candidate_summary)

output = open("Analysis/Eanalysis.txt", 'w')
output.write(f'''
        Analysis
        ------------------
        Total Votes: {total_votes}
        Candidates: {candidate_votes_dict}
        Names:{candidate_results}
        List:{candidate}
        percentage: {vote_percentage}
       Winner: {winning_candidate}
       Winning Vote Count: ${winning_count}
       Winning percentage: ${winning_percentage}''')



    



    