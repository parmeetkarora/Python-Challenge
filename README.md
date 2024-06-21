Create a new repository for this project called python-challenge. Do not add this homework assignment to an existing repository.

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period
FOR PYBANK
import os
import csv


INPUT_CSV_PATH = os.path.join('Resources', 'budget_data.csv')

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(INPUT_CSV_PATH, 'r') as input_file:
    csv_reader = csv.reader(input_file)
    header = next(csv_reader)

        #Setting variables
    TotalMonths = []
    TotalAmount = []
    MonthlyChangeProfit = []


    MonthlyChange = 0
    MonthlyChangeTotal = 0
    InitialProfitCounter = 0


    for row in csv_reader:
        
        TotalMonths.append(row[0])
        SumMonths = len(TotalMonths)
        TotalAmount.append(float(row[1]))
        ProfitForMonth = int(row[1])
        MonthlyChange = float(ProfitForMonth)
        MonthlyChangeTotal = MonthlyChangeTotal + MonthlyChange
        InitialProfitCounter = int(row[1])
        MonthlyChangeProfit.append(MonthlyChange)
        MaxProfit = max(MonthlyChangeProfit)
        MaxIndex = MonthlyChangeProfit.index(MaxProfit)
        MinProfit = min(MonthlyChangeProfit)
        MinIndex = MonthlyChangeProfit.index(MinProfit)
        AvgChangeProfit = round(MonthlyChangeTotal/SumMonths)
        SumAmount = sum(TotalAmount)

        print(f'Analysis')
        print(f'--------')
        print(f'Total Months: {SumMonths}')
        print(f'Total Amount: ${SumAmount}')
        print(f'Average Monthly Change: ${SumAmount}')
        print(f'Greatest Increase in Profits: {TotalMonths[MaxIndex]} ${MaxProfit}')
        print(f'Greatest Decrease in Profits: {TotalMonths[MinIndex]} ${MinProfit}')


        output = open("Analysis/Analysis.txt", 'w')
        output.write(f'''
        Analysis
        ------------------
        Total Months: {SumMonths}
        Total: ${SumAmount}
        Average Monthly Change: ${AvgChangeProfit}
        Greatest Increase in Profits: {TotalMonths[MaxIndex]} (${MaxProfit})
        Greatest Decrease in Profits: {TotalMonths[MinIndex]} (${MinProfit})''')
        
        Analysis
        ------------------
        Total Months: 86
        Total: $22564198.0
        Average Monthly Change: $262374
        Greatest Increase in Profits: Mar-13 ($1141840.0)
        Greatest Decrease in Profits: Dec-10 ($-1194133.0)


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


Your analysis should align with the following results:
