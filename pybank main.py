import os
import csv

csvpath = os.path.join("budget_data.csv")

date = []
monthly_pnl = []
total_months = 0
total_profitloss = 0
change_profitloss = 0
total_change = 0
greatest_increase = ["",0]
greatest_decline = ["",0]

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        monthly_pnl.append(row[1])

        total_months += 1
        total_profitloss += int(row[1])

        total_change = int(row[1]) - change_profitloss
        if change_profitloss == 0:
            total_change = 0
        change_profitloss = int(row[1])
        total_change += change_profitloss

        if total_change > int(greatest_increase[1]):
            greatest_increase[1] = total_change
            greatest_increase[0] = row[0]

        if change_profitloss < int(greatest_decline[1]):
            greatest_decline[1] = change_profitloss
            greatest_decline[0] = row[0]

    total_change = total_change / (total_months -1)

print("\n\nbudget data")
print(f"months total: {total_months}")
print(f"total: ${total_profitloss}")
print(f"most increase in profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"most increase in profits: {greatest_decline[0]} (${greatest_decline[1]})")