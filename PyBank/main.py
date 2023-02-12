#import os module and module for csv files
import os
import csv 
#store the relative filepath into a variable
csvFilePath = os.path.join("Resources","budget_data.csv")
#open and read csv
with open(csvFilePath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
#setting count of months and net profit to zero 
    totalMonths = 0
    profitTotal = 0
#creating 2 lists to hold the net profit values and the months    
    totalChanges = []
    dates = [] 
#skip first line since it is the header
    next(csvReader)
#setting up the first row after the header as the initial previous value, also calculating the count of months and profit
    first_row = next(csvReader)
    previousValue = int(first_row[1])
    totalMonths += 1
    profitTotal = profitTotal + int(first_row[1])
#loop to go through all the other lines calculating the count of months and profit
    for row in csvReader:   
        totalMonths += 1
        profitTotal = profitTotal + int(row[1])
#calculating the net profit and adding the value to the totalChanges list and the months to the dates list
        currentValue = int(row[1])
        netvalue = currentValue - previousValue
        totalChanges.append(netvalue)
        previousValue = currentValue
        dates.append(row[0])
#calculating the average of the net profit, greatest increase in profits (max) and greatest decrease in profits (min)
    avgChange = sum(totalChanges)/len(totalChanges)
    maxChange = max(totalChanges)
    minChange = min(totalChanges)
#printing the results into the console 
    print(f"\nFinancial Analysis\n")
    print(f"\n--------------------\n")
    print(f"\nTotal Months:{totalMonths}\n")
    print (f"\nTotal:${profitTotal}\n")
    print (f"\nAverage Change: ${avgChange :.2f}\n")
    print (f"\nGreatest Increase in Profits: {dates[totalChanges.index(maxChange)]} (${maxChange})\n")
    print (f"\nGreatest Decrease in Profits: {dates[totalChanges.index(minChange)]} (${minChange})\n")
#output the results into a text file in the Analysis folder 
outputFilePath = os.path.join("Analysis", "output.txt")
#open and write mode 
with open(outputFilePath, "w") as textFile:
#output to be written into the text file
    output = ""
    output += f"\nFinancial Analysis\n"
    output += f"\n--------------------\n"
    output += f"\nTotal Months:\t{totalMonths}\n"
    output += f"\nTotal: ${profitTotal}\n"
    output += f"\nAverage Change: ${avgChange :.2f}\n"
    output += f"\nGreatest Increase in Profits: {dates[totalChanges.index(maxChange)]} (${maxChange})\n"
    output += f"\nGreatest Decrease in Profits: {dates[totalChanges.index(minChange)]} (${minChange})\n"
#writting the output above into the txt file
    textFile.write(output)


  
