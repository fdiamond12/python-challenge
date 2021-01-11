import os
import csv

budget_file = os.path.join('Resources','budget_data.csv')


with open(budget_file,'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    #ignore header
    csvheader = next(csv_file)
   

   #set all variables to zero so they can accumulate as we go through the rows
    month_count = 0
    tot_prof_loss = 0
    prev_prof_loss = 0
    max_loss = 0
    max_gain = 0
    tot_prof_loss_change = 0

    for row in csvreader:
        #Add number of months in file
        month_count = month_count + 1

        #Add total profit/loss in the file
        tot_prof_loss = tot_prof_loss + int(row[1])

        #No profit/loss change for first month of file
        if month_count == 1:
            prof_loss_change = 0
        
        #All other months profit/loss change will equal to current month P/L - previous month's P/L 
        else:
            prof_loss_change = int(row[1]) - prev_prof_loss
        
       #Compare current month P/L change to see if it is higher/lower than previous months
        if prof_loss_change > max_gain:
            max_gain = prof_loss_change
            max_gain_mo = str(row[0])
        elif prof_loss_change < max_loss:
            max_loss = prof_loss_change
            max_loss_mo = str(row[0])
        
        #Add current month P/L change to total
        tot_prof_loss_change = tot_prof_loss_change + prof_loss_change
        
        #Set current month P/L to "Previous Month P/L" so the next month can be compared to this month
        prev_prof_loss = int(row[1])
        
    #Calculate average total change in P/L for the period   
    avg_prof_loss_change = round(tot_prof_loss_change/(month_count-1),2)
    
    #Print Stats 
    #How to print data on multiple lines source: https://stackoverflow.com/questions/34980251/how-to-print-multiple-lines-of-text-with-python/34980291
    print(f"Financial Analysis\nTotal Months: {month_count}\nTotal P/L: ${tot_prof_loss}\nAverage Change: ${avg_prof_loss_change}\nGreatest Increase in Profits: {max_gain_mo} (${max_gain})\nGreatest Decrease in Profits: {max_loss_mo} (${max_loss})")



results_file = open(os.path.join("Analysis","Results.txt"),"w")

results_file.write(f"Financial Analysis\nTotal Months: {month_count}\nTotal P/L: ${tot_prof_loss}\nAverage Change: ${avg_prof_loss_change}\nGreatest Increase in Profits: {max_gain_mo} (${max_gain})\nGreatest Decrease in Profits: {max_loss_mo} (${max_loss})")