import csv
import os
import statistics


#set variables
row_counter = 0
candidate = ""
max_name = ""
max_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
khan_percentage = 0
correy_percentage = 0
li_percentage = 0
otooley_percentage = 0

# Path to collect data from the Resources folder
election_csv_path = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(election_csv_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    header = next(csvreader)

    #read one line at a time
    for row in csvreader:

        # The total number of votes cast
        row_counter = row_counter + 1

        #create a variable to hold the candidate's name
        candidate = str(row[2])
        
        #Tally the votes for each candidate
        if candidate =="Khan":
            khan_votes = khan_votes + 1

        if candidate == "Correy":
            correy_votes = correy_votes + 1

        if candidate == "Li": 
            li_votes = li_votes + 1            

        if candidate == "O'Tooley":
            otooley_votes = otooley_votes + 1

    #Determine if Khan is the winner
    if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes:
        max_votes = khan_votes
        max_name = ("Khan")

    #Determine if Correy is the winner
    if correy_votes > khan_votes and correy_votes > li_votes and correy_votes > otooley_votes:
        max_votes = correy_votes
        max_name = ("Correy")

    #Determine if Li is the winner
    if li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes:
        max_votes = li_votes
        max_name = ("Li")

    #Determine if O'Tooley is the winner    
    if otooley_votes > khan_votes and otooley_votes > correy_votes and otooley_votes > li_votes:
        max_votes = otooley_votes
        max_name = ("O'Tooley")

#Determine the percentage of votes for each candidate 
khan_percentage = round((khan_votes / row_counter) * 100,2)
correy_percentage = round((correy_votes / row_counter) * 100,2)
li_percentage = round((li_votes / row_counter) * 100,2)
otooley_percentage = round((otooley_votes / row_counter) * 100,2) 
  
print("")
print("")
print("Election Results")
print("-------------------------")
print("Total Votes:  " + str(row_counter))
print("-------------------------")
print("Khan:  " + str(khan_percentage) + "%  (" + str(khan_votes) + ")")
print("Correy:  " + str(correy_percentage) + "%  (" + str(correy_votes) + ")")
print("Li:  " + str(li_percentage) + "%  (" + str(li_votes) + ")")
print("O'Tooley:  " + str(otooley_percentage) + "%  (" + str(otooley_votes) + ")")
print("-------------------------")
print("Winner:  " + str(max_name))
print("-------------------------")

with open("Analysis/polls.txt", "w") as text_file:
    text_file.write("")
    text_file.write("")
    text_file.write("\n")
    text_file.write("")
    text_file.write("\n")
    text_file.write("Election Results")
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")
    text_file.write("Total Votes:  " + str(row_counter))
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")
    text_file.write("Khan:  " + str(khan_percentage) + "%  (" + str(khan_votes) + ")")
    text_file.write("\n")
    text_file.write("Correy:  " + str(correy_percentage) + "%  (" + str(correy_votes) + ")")
    text_file.write("\n")
    text_file.write("Li:  " + str(li_percentage) + "%  (" + str(li_votes) + ")")
    text_file.write("\n")
    text_file.write("O'Tooley:  " + str(otooley_percentage) + "%  (" + str(otooley_votes) + ")")
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")
    text_file.write("Winner:  " + str(max_name))
    text_file.write("\n")
    text_file.write("-------------------------")
    text_file.write("\n")

