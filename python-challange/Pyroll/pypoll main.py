import os
import csv
#same issue as the pybank problem not being able to connect to the file with just the parent directory. 
csvpath = os.path.join('/Users/stevengonzalez/Desktop/python-challange/Pyroll/Resources/election_data.csv')

ttl_votes = 0
ballot_id = []
per_count = []
num_count = []
each_can = []
candidates = []

#same method as pybank
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
  
    for row in csvreader:
        
        ttl_votes = ttl_votes + 1
        
        candidates.append(row[2])
     
    for x in set(candidates):
        each_can.append(x)
        #error either reads to define the variable, or that it can't be called on.... follow-up
        y = candidates.count(x)
        num_count.append(y)
        #might be the same issue as above. 
        z = (y/ttl_votes)*100
        per_count.append(z)
        
    win_count = max(num_count)
    win = each_can[num_count.index(win_count)]
 
print("Election Results:")   
print("Total Votes :" + str(ttl_votes))    
#reason for i- rewatch lesson. Reference DataCamp for building output. 
for i in range(len(each_can)):
            print(each_can[i] + ": " + str(per_count[i]) +"% (" + str(num_count[i])+ ")")
print("-------------------------")
print("The winner is: " + win)
print("-------------------------")

new_file = open("pypollelectionresults.txt", "w")
new_file.write("Election Results:")   
new_file.write("Total Votes :" + str(ttl_votes))    
#reason for i- rewatch lesson. Reference DataCamp for building output. 
for i in range(len(each_can)):
            new_file.write(each_can[i] + ": " + str(per_count[i]) +"% (" + str(num_count[i])+ ")")
new_file.write("-------------------------")
new_file.write("The winner is: " + win)
new_file.write("-------------------------")