#remember to store effectively! Lists can work. Reference DataCamp practice. 

import os
import csv

#Needed a a more well defined path, rather than the parent directory shared. Not sure why. https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory
csvpath = os.path.join('/Users/stevengonzalez/Desktop/python-challange/PyBank/Resources/budget_data.csv')
#solution - there was a duplicate file path. 
begin_pro = 0
ttl_pro = 0
month = 0
ttl_change = 0
pro = []
mo_changes = []
mo_dates = []


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:    
      
      month = month + 1 
    #append issue with row. Needs to be addressed. 
      mo_dates.append(row[0]);

      pro.append(row[1]);
      
      ttl_pro = ttl_pro + int(row[1]);

      final = int(row[1]);
      
      monthly_change_profits = final - begin_pro;

      mo_changes.append(monthly_change_profits);

      ttl_change = ttl_change + monthly_change_profits;
      
      begin_pro = final;

      avg_change = (ttl_change / month);
      
      highest_increase = max(mo_changes);
      biggest_decrease = min(mo_changes);

      increase_month = mo_dates[mo_changes.index(highest_increase)];
      decrease_month = mo_dates[mo_changes.index(biggest_decrease)];
      

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months: " + str(month))
    print("Total Profits: " + "$" + str(ttl_pro))
    print("Average Change: " + "$" + str(int(avg_change)))
    print("Greatest Increase in Profits: " + str(increase_month) + " ($" + str(highest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_month) + " ($" + str(biggest_decrease) + ")")

new_file = open("pybankoutput.txt","w")

new_file.write("Financial Analysis \n")
new_file.write("-------------------------------------------- \n")
new_file.write(f"Total Months: {month} \n")
new_file.write(f"Total: {ttl_pro} \n")
new_file.write(f"Average Change: {avg_change} \n")
new_file.write(f"Greatest Increase in Profits: {highest_increase} \n")
new_file.write(f"Greatest Decrease in Profits: {biggest_decrease} \n")
