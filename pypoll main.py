import os
import csv

csvpath = os.path.join('election_data.csv')

totalvotes = []
candidatelist = []
percentvote = []
totaleachcandidate = []
wiinercandidate = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        totalvotes += 1

        if row[2] not in candidatelist:
            candidatelist.append(row[2])
            totaleachcandidate[row[2]]=0
        totaleachcandidate[row[2]]+=1

print("election outcome")
print(f"all votes: {totalvotes}")
output.write(f"election outcome")
output.write(f"total: {totalvotes}")
