import os
import csv

election_file = os.path.join('Resources','election_data.csv')


with open(election_file,'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    #ignore header
    csvheader = next(csv_file)

    vote_count = 0
    candidatelist = {"Candidates": [], "Votes":[]}
    candidate_count = 0

    for row in csvreader:
        vote_count = vote_count + 1
        #Add only unique values to list source: https://stackoverflow.com/questions/42334197/add-only-unique-values-to-a-list-in-python
        if str(row[2]) not in candidatelist["Candidates"]:
            candidatelist["Candidates"].append(row[2])
            candidatelist["Votes"].append(1)
        elif str(row[2]) in candidatelist["Candidates"]:
            for candidate in candidatelist["Candidates"]:
                if str(row[2]) == str(candidate):
                    name = str(row[2])
                    index = candidatelist["Candidates"].index(name)
                    candidate_count = int(candidatelist["Votes"][index]) + 1
                    votes = candidatelist["Votes"]
                    votes[index] =candidate_count


listlength = len(candidatelist["Candidates"])

print(f"Election Results\n-------------------\nTotal Votes: {vote_count}\n-------------------\n")

winner_vote = 0
for i in range(0,listlength):
    #format as percentage source: https://www.kite.com/python/answers/how-to-format-a-number-as-a-percentage-in-python
    percent_votes = "{:.3%}".format(candidatelist["Votes"][i] / vote_count)
    print(f'{candidatelist["Candidates"][i]}: {percent_votes} ({candidatelist["Votes"][i]})')
    if candidatelist["Votes"][i] > winner_vote:
        winner_name = candidatelist["Candidates"][i]
        winner_vote = candidatelist["Votes"][i]
print(f"-------------------\nWinner: {winner_name}")


results_file = open(os.path.join("Analysis","Results.txt"),"w")
results_file.write(f"Election Results\n-------------------\nTotal Votes: {vote_count}\n-------------------\n")



winner_vote = 0
for i in range(0,listlength):
    #format as percentage source: https://www.kite.com/python/answers/how-to-format-a-number-as-a-percentage-in-python
    percent_votes = "{:.0%}".format(candidatelist["Votes"][i] / vote_count)
    results_file.write(f'{candidatelist["Candidates"][i]}: {percent_votes} ({candidatelist["Votes"][i]})\n')
    if candidatelist["Votes"][i] > winner_vote:
        winner_name = candidatelist["Candidates"][i]
        winner_vote = candidatelist["Votes"][i]
results_file.write(f"-------------------\nWinner: {winner_name}")
