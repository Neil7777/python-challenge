# import Dependencies
import os, csv
from pathlib import Path

#declare file path
input_file = Path("PyBank", "Resources", "budget_data.csv")
#PyBank\Resources\budget_data.csv

#create variables for the specific rows
totalmonths = []
totalPnL = []
monthlyPnLchange = []

#open cvs file
with open(input_file,newline="", encoding="utf-8") as budget:

    #store the data of budget_data file in varaible
    csvreader = csv.reader(budget,delimiter=",")

    #skip header
    header = next(csvreader)
    
    for row in csvreader:
        
        #append the data
        totalmonths.append(row[0])
        totalPnL.append(int(row[1]))

        #print (totalmonths,totalPnL)

    for i in range(len(totalPnL)-1):

        monthlyPnLchange.append(totalPnL[i+1]-totalPnL[1])


max_profit = max(monthlyPnLchange)
max_loss = min(monthlyPnLchange)

print(max_loss)
print(max_profit)

max_increase_month = monthlyPnLchange.index(max(monthlyPnLchange)) +1
max_decrease_month = monthlyPnLchange.index(min(monthlyPnLchange)) +1


print("Financial Analysis")
print("-------------------------------------")
print(f"Total Month: {len(totalmonths)}")
print(f"Total: ${sum(totalPnL)}")
print(f"Average Change: {round(sum(monthlyPnLchange)/len(monthlyPnLchange),2)}")
print(f"Greatest Increase in Profits: {totalmonths[max_increase_month]} (${(str(max_profit))})")
print(f"Greatest Decrease in Profits: {totalmonths[max_decrease_month]} (${(str(max_loss))})")