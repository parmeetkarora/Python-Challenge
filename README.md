Create a new repository for this project called python-challenge. Do not add this homework assignment to an existing repository.

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period
FOR PYBANK

# Import dependencies
import os
import csv

# Setting variables
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
profit_loss_change = 0


os.chdir(os.path.dirname(__file__))

budget_data_csv_path = os.path.join("Resources", "budget_data.csv")


# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    print(f"Header: {csv_header}")
    
             
    
    for row in csv_reader:

        # Count of months
        count_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
           
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

    
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign highest and lowest month
    highest_month = months[highest_month_index]
    lowest_month = months[lowest_month_index]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {highest_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {lowest_month} (${lowest_change})")

# Output results in file
output = open("Analysis/Analysis.txt", 'w')
output.write(f'''
        Financial Analysis
        ------------------
        Total Months: {count_months})
        Total: ${net_profit_loss})
        Average Monthly Change: ${average_profit_loss})
        Greatest Increase in Profits: {highest_month} (${highest_change})
        Greatest Decrease in Profits: {lowest_month} (${lowest_change})''')


        Financial Analysis
        ------------------
        Total Months: 86)
        Total: $22564198)
        Average Monthly Change: $-8311.11)
        Greatest Increase in Profits: Aug-16 ($1862002)
        Greatest Decrease in Profits: Feb-14 ($-1825558)

        FOR PYPOLL

        You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

Your analysis should align with the following results:
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


# Initialize variables for the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Loop through each candidate to find the winner
for candidate, votes in candidate_votes_dict.items():
    vote_percentage = (votes / total_votes) * 100
    candidate_results = (f"{candidate}: {vote_percentage:.1f}%  ({votes:,})\n")
        
    print(candidate_results)

    # Check if the current candidate has more votes and a higher percentage than the current winner
    if votes > winning_count and vote_percentage > winning_percentage:
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

# Print the winner's summary
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n"
)
print(winning_candidate_summary)
output = open("Analysis/Eanalysis.txt", 'w')
output.write(f'''
        Election results
        ---------------------------
        Total Votes: {total_votes}
        ---------------------------
        Candidates: {candidate_votes_dict}
        Names:{candidate_results}
        List:{candidate}
        percentage: {vote_percentage}
       Winner: {winning_candidate}
       Winning Vote Count: ${winning_count}
       Winning percentage: ${winning_percentage}''')

        Election results
        ---------------------------
        Total Votes: 369711
        ---------------------------
        Candidates: {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}
        Names:Raymon Anthony Doane: 3.1%  (11,606)

        List:Raymon Anthony Doane
        percentage: 3.1392087333079077
       Winner: Diana DeGette
       Winning Vote Count: $272892
       Winning percentage: $73.81224794501652
