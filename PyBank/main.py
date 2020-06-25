import csv
import os
import statistics


#set variables
row_counter = 0
net_total = 0
change = 0
change_amounts = []
dates_change = []
average_change = 0
max_change = 0
min_change = 0
amount1 = 0
amount2 = 0
max_date = ""
min_date = ""


# Path to collect data from the Resources folder
budget_csv_path = os.path.join('Resources', 'budget_data.csv')

# Open and read csv
with open(budget_csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    header = next(csvreader)

    #read one line at a time
    for row in csvreader:

        # The total number of months included in the dataset
        row_counter = row_counter + 1

        # The net total amount of "Profit/Losses" over the entire period
        net_total = net_total + int(row[1])

        #create a variable to hold the amounts from column 2
        amount2 = int(row[1])

        #create a variable to hold the dates from column 1
        date = str(row[0])

        #calculate the amount of change from one row to the next    
        change = int(amount2) - int(amount1)

        #Delete the value of row 1 since 0 to row 1 is not a change in value
        if amount1 == 0:
            change = change - int(amount2)

        #add the change to the list of change amounts
        change_amounts.append(change)

        #add the date to the list of dates
        dates_change.append(date)

        #change the value of amount 1 to equal the end value from the previous change
        amount1 = amount2

# The greatest increase in profits (date and amount) over the entire period
max_change = max(change_amounts)
max_date = dates_change[change_amounts.index(max_change)]

# The greatest decrease in losses (date and amount) over the entire period
min_change = min(change_amounts)
min_date = dates_change[change_amounts.index(min_change)]

# The average of the changes in "Profit/Losses" over the entire period / subtract 1 from the row-counter to 
    #exclude row 1
average_change = sum(change_amounts) / int(row_counter-1)
average_change = round(average_change,2) 

print("")
print("")
print("Financial Analysis")
print("------------------------------")
print("Total Months:  " + str(row_counter))
print("Total:  $" + str(net_total))
print("Average:  $" + str(average_change))
print("Greatest Increase in Profits:  "+ str(max_date) + " ($" + str(max_change) + ") ")
print("Greatest Decrease in Profits:  "+ str(min_date) + " ($" + str(min_change) + ") ")
print("")

with open("Analysis/financial.txt", "w") as text_file:
    text_file.write("")
    text_file.write("\n")
    text_file.write("")
    text_file.write("\n")
    text_file.write("Financial Analysis")
    text_file.write("\n")
    text_file.write("------------------------------")
    text_file.write("\n")
    text_file.write("Total Months:  " + str(row_counter))
    text_file.write("\n")
    text_file.write("Total:  $" + str(net_total))
    text_file.write("\n")
    text_file.write("Average:  $" + str(average_change))
    text_file.write("\n")
    text_file.write("Greatest Increase in Profits:  "+ str(max_date) + " ($" + str(max_change) + ") ")
    text_file.write("\n")
    text_file.write("Greatest Decrease in Profits:  "+ str(min_date) + " ($" + str(min_change) + ") ")
    text_file.write("\n")
    text_file.write("")
    text_file.close()