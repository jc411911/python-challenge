import os
import csv

# Path to the CSV file
budget = os.path.join("Resources", "budget_data.csv")

# Open the CSV file and read its content
with open(budget, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header
    
    # Setting variables
    total_months = 0
    net_amount = 0
    changes = []
    previous_value = None
    greatest_increase = {'date': '', 'amount': float('-inf')}
    greatest_decrease = {'date': '', 'amount': float('inf')}

    # Loop through each row in the CSV file
    for row in csv_reader:
        total_months += 1  # Increment the total month count
        current_value = float(row[1])  # Get the current month's profit/loss
        net_amount += current_value  # Add the net total amount

        if previous_value is not None:
            change = current_value - previous_value  # Calculate change from previous month
            changes.append(change)  # Append change
            
            # Check for greatest increase in profits
            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = row[0]
                
            # Check for greatest decrease in profits
            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = row[0]

        previous_value = current_value  

    # Calculate the average change in profits/losses
    average_change = round(sum(changes) / len(changes), 2) if changes else 0

# Prepare the output
output = []
output.append("Financial Analysis")
output.append("----------------------------")
output.append("Total Months: " + str(total_months))
output.append("Total: $" + str(int(net_amount)))
output.append("Average Change: $" + str(average_change))
output.append("Greatest Increase in Profits: " + greatest_increase['date'] + " ($" + str(int(greatest_increase['amount'])) + ")")
output.append("Greatest Decrease in Profits: " + greatest_decrease['date'] + " ($" + str(int(greatest_decrease['amount'])) + ")")


output_text = "\n".join(output)

# Print the output to the terminal
print(output_text)

# Write the output to a text file
with open("financial_analysis.txt", "w") as text_file:
    text_file.write(output_text)
