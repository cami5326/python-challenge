#import os module and module for csv files
import os
import csv 
#store the relative filepath into a variable
csvFilePath = os.path.join("Resources","election_data.csv")
#open and read csv
with open(csvFilePath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
#setting count of total votes and percentage to zero 
    totalVotes = 0
    percentage = 0
#creating 1 list to hold the candidate names and and 1 dictionary to hold their count of votes along with their names       
    candidateList = [] 
    votesPerCandidateDic = {}
#skip first line since it is the header   
    next(csvReader)
#loop to go through all the lines calculating the count of votes
    for row in csvReader:   
        totalVotes += 1
# for each row, if the candidate name is not in the list of candidate names, add the name to the list
        if row[2] not in candidateList:
            candidateList.append(row[2])
#if the candidate name is not in the list of candidate names, set their count of votes to zero
            votesPerCandidateDic [row[2]] = 0
 #for each row, add 1 to count of votes for each candidate name      
        votesPerCandidateDic [row[2]] +=1    
#calculating the candidate with more votes (max) using the dictionary information
    winner=max(zip(votesPerCandidateDic.values(), votesPerCandidateDic.keys()))[1]
#printing the results into the console
    print(f"\nElection Results")
    print(f"\n--------------------")
    print(f"\nTotal Votes: {totalVotes}")
    print(f"\n--------------------")
#printing the dictionary results (candidate name and count of votes), also calculating the percentage of votes for each candidate out of total votes
    for key,values in votesPerCandidateDic.items():
        percentage = (values/totalVotes)*100
        print(f"{key}: {percentage :.3f}% ({values})")
#printing the candidate with more votes (winner) results into the console
    print(f"\n--------------------")
    print(f"\nWinner: {winner}")
    print(f"\n--------------------")
#output the results into a text file in the Analysis folder 
outputFilePath = os.path.join("Analysis", "output.txt")
#open and write mode 
with open(outputFilePath, "w") as textFile:
#output to be written into the text file
    output = ""
    output += f"Election Results\n"
    output += f"\n--------------------\n"
    output += f"\nTotal Votes: {totalVotes}\n"
    output += f"\n--------------------\n"
    for key,values in votesPerCandidateDic.items():
        percentage = (values/totalVotes)*100
        output += f"\n{key}: {percentage :.3f}% ({values})\n"
    output += f"\n--------------------\n"
    output += f"\nWinner: {winner}\n"
    output += f"\n--------------------\n"
#writting the output above into the txt file
    textFile.write(output)



          