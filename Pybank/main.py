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
