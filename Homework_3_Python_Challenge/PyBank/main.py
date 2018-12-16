#This code allows you to go over a file in the file path line by line, storing each line in a list
import os
import csv

csvpath= "budget_data.csv" 

total_no_months=[]
total_profit=[]
change=[]
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_no_months.append(row[0])
        total_profit.append(int(row[1]))


months=len(total_no_months)

for x in range(months-1):
        change.append(total_profit[x+1]-total_profit[x])

profit=sum(total_profit)
avg_change=sum(change)/len(change)
increase= max(change)
decrease= min(change)

for x in range(months-1):
    if change[x]==increase:
        month1=total_no_months[x+1]
        #print(f"The month1 is {month1}\n") 
for x in range(months-1):
    if change[x]==decrease:
        month2=total_no_months[x+1]
        #print(f" The month2 is {month2}\n")

output_path = "budget_analysis_data.txt"

with open(output_path, 'w', newline="") as txtfile:
    txtfile.write("Financial Analysis \n")
    txtfile.write("---------------------------------------------------------------------\n")
    txtfile.write(f"Total Months:{months}\n")
    txtfile.write(f"Total:${profit}\n")
    txtfile.write(f"Average Change:${round(100*(avg_change))/100}\n")
    txtfile.write(f"Greatest Increase in Profits:{month1} (${increase})\n")
    txtfile.write(f"Greatest Decrease in Profits:{month2} (${decrease})\n")
    print("\n")    
    print("Financial Analysis \n")
    print("---------------------------------------------------------------------\n")
    print(f"Total Months:{months}\n")
    print(f"Total:${profit}\n")
    print(f"Average Change:${round(100*(avg_change))/100}\n")
    print(f"Greatest Increase in Profits:{month1} (${increase})\n")
    print(f"Greatest Decrease in Profits:{month2} (${decrease})\n")

