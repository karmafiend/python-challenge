#PyBank script file - Chris Kilkes

#PyBank module instructions:
#In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Outline the coding:
import os
import csv

#Create the path to the CSV file
csv_filename = 'budget_data.csv'
csv_path = os.path.join(os.path.dirname(__file__), 'Resources', csv_filename)

#Initialize variables
total_months = 0
net_total = 0
total_loss = 0
total_profit = 0
total_pnl = 0
pProfit_loss = None #previous profit loss
profit_change = []
greatest_increase_profit = {"Date": "", "Profits/Losses": 0} #need to add date and amount
greatest_decrease_profit = {"Date": "", "Profits/Losses": 0} #need to add date and amount

#Read the CSV file
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) #Skip the header row

#Begin calculating on data in .csv file

#Loop through each row in the CSV
    
    for row in csvreader:
    #Update total months and net total
        total_months += 1
        net_total += int(row[1])

    # 'print(row)

#Calculate profit changes
        profit_loss = int(row[1])
        if pProfit_loss is not None: 
            change = profit_loss - pProfit_loss
            profit_change.append(change)

#Update greatest increase and decrease

            if change > int(greatest_increase_profit["Profits/Losses"]):
                greatest_increase_profit["Date"] = row[0]
                greatest_increase_profit["Profits/Losses"] = change

            if change < int(greatest_decrease_profit["Profits/Losses"]):
                greatest_decrease_profit["Date"] = row[0]
                greatest_decrease_profit["Profits/Losses"] = change

        pProfit_loss = profit_loss

#Calculate average change

average_change = sum(profit_change) / len(profit_change)

#Print the analysis to the terminal

print("PyBank Financial Analysis")
print("----------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:{greatest_increase_profit['Date']}(${greatest_increase_profit['Profits/Losses']})")
print(f"Greatest Decrease in Profits:{greatest_decrease_profit['Date']}(${greatest_decrease_profit['Profits/Losses']})")                                                        

#Export the results to a text file
                                                                          
output_filename = "financial_analysis_results.txt"
analysis_folder = os.path.join(os.path.dirname(__file__), 'analysis')
output_file_path = os.path.join(analysis_folder, output_filename)

with open(output_file_path, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_profit['Date']} (${greatest_increase_profit['Profits/Losses']})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_profit['Date']} (${greatest_decrease_profit['Profits/Losses']})\n")

print(f"Results have been exported to '{output_file_path}'")                                                                        