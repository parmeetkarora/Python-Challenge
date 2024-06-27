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
