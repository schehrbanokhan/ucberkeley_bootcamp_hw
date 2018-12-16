import os
import csv

csvpath= "election_data.csv" 

all_voter_id=[]
all_candidates=[]
votes_for_khan=0
votes_for_correy=0
votes_for_li=0
votes_for_tooley=0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        all_voter_id.append(row[0])
        all_candidates.append(row[2])

    total_votes=len(all_voter_id)

for x in range(total_votes):
    if all_candidates[x] =="Khan" or all_candidates[x]=="khan":
        votes_for_khan+=1
    if all_candidates[x] =="Correy" or all_candidates[x]=="correy":
        votes_for_correy+=1
    if all_candidates[x] =="Li" or all_candidates[x]=="li":
        votes_for_li+=1
    if all_candidates[x] =="O'Tooley" or all_candidates[x]=="o'tooley":
        votes_for_tooley+=1

khan_percentage= round((votes_for_khan/total_votes)*100)
correy_percentage= round((votes_for_correy/total_votes)*100)
li_percentage= round((votes_for_li/total_votes)*100)
tooley_percentage= round((votes_for_tooley/total_votes)*100)


can=["Khan","Correy","Li","O'Tooley"]
vot_per=[khan_percentage,correy_percentage,li_percentage,tooley_percentage]

for x in range(len(can)):
    if vot_per[x]==max(vot_per):
        winner = can[x]
        print(winner)


output_path = "election_analysis_data.txt"

with open(output_path, 'w', newline="") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("---------------------------------------------------------------------\n")
    txtfile.write(f"Total Votes:{total_votes}\n")
    txtfile.write("---------------------------------------------------------------------\n")
    txtfile.write(f"Khan: {khan_percentage}% ({votes_for_khan})\n")
    txtfile.write(f"Correy: {correy_percentage}% ({votes_for_correy})\n")
    txtfile.write(f"Li: {li_percentage}% ({votes_for_li})\n")
    txtfile.write(f"O'Tooley: {tooley_percentage}% ({votes_for_tooley})\n")
    txtfile.write("---------------------------------------------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("---------------------------------------------------------------------\n")
    
    print("Election Results\n")
    print("---------------------------------------------------------------------\n")
    print(f"Total Votes:{total_votes}\n")
    print("---------------------------------------------------------------------\n")
    print(f"Khan: {khan_percentage}% ({votes_for_khan})\n")
    print(f"Correy: {correy_percentage}% ({votes_for_correy})\n")
    print(f"Li: {li_percentage}% ({votes_for_li})\n")
    print(f"O'Tooley: {tooley_percentage}% ({votes_for_tooley})\n")
    print("---------------------------------------------------------------------\n")
    print(f"Winner: {winner}\n")
    print("---------------------------------------------------------------------\n")


