# import Dependencies
import os, csv
from pathlib import Path

#declare file path
input_file = Path("PyBank", "Resources", "budget_data.csv")
#PyBank\Resources\budget_data.csv

#create variables for the specific rows
totalmonths = []
totalPnL = []
mounthlyPnLchange = []

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

       # print (totalmonths,totalPnL)