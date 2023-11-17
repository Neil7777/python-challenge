# Import Dependdenciies
import os, csv
from pathlib import Path

#
csv_file_path = Path("PyPoll", "Resources", "election_data.csv")
#PyPoll\Resources\election_data.csv

#Declare Variable
TotalVote = 0
Stockham = 0
DeGette = 0
Doane = 0


# open csv file
with open(csv_file_path, newline="", encoding="utf-8") as election:

    #store the data of election_data file in varaible
    csvreader = csv.reader(election,delimiter=",")

    #Skip header
    header= next(csvreader)

    for row in csvreader:

        #count total votes
        TotalVote = TotalVote + 1
        
        if row[2] == "Charles Casper Stockham":
            Stockham = Stockham + 1
        elif row[2] == "Diana DeGette":
            DeGette = DeGette + 1
        elif row[2] == "Raymon Anthony Doane":
            Doane = Doane + 1

# find the winner
Candidate = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
Votes = [Stockham, DeGette, Doane]

candzip = dict(zip(Candidate,Votes))
winner = max(candzip, key=candzip.get)

#calculate the percent of votes
StockhamPercent = ((Stockham/TotalVote)*100)
DeGettePercent = ((DeGette/TotalVote)*100)
DoanePercent = ((Doane/TotalVote)*100)

#print statement
print("Election Results")
print("-------------------------")
print(f"Total Votes: {TotalVote}")
print("-------------------------")
print(f"Charles Casper Stockham: {StockhamPercent:.3f}% {Stockham}")
print(f"Diana DeGette: {DeGettePercent:.3f}% {DeGette}")
print(f"Raymon Anthony Doane: {DoanePercent:.3f}% {Doane}")
print("-------------------------")
print(f"Winner: {winner}")

#Output file
output_file = Path("Pypoll", "analysis", "Analysis.txt")

with open(output_file,"w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes: {TotalVote}")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {StockhamPercent:.3f}% {Stockham}")
    file.write("\n")
    file.write(f"Diana DeGette: {DeGettePercent:.3f}% {DeGette}")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {DoanePercent:.3f}% {Doane}")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")