import os
import csv

budget = os.path.join("Resources", "budget_data.csv")

with open(budget, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    total_months = 0
    net_amount = 0
    changes = []
    previous_value = None
    greatest_increase = {'date': '', 'amount': float('-inf')}
    greatest_decrease = {'date': '', 'amount': float('inf')}

    for row in csv_reader:
        total_months += 1
        current_value = float(row[1])
        net_amount += current_value

        if previous_value is not None:
            change = current_value - previous_value
            changes.append(change)
            
            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = row[0]
                
            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = row[0]

        previous_value = current_value

    average_change = round(sum(changes) / len(changes), 2) if changes else 0

output = []
output.append("Financial Analysis")
output.append("----------------------------")
output.append("Total Months: " + str(total_months))
output.append("Total: $" + str(int(net_amount)))
output.append("Average Change: $" + str(average_change))
output.append("Greatest Increase in Profits: " + greatest_increase['date'] + " ($" + str(int(greatest_increase['amount'])) + ")")
output.append("Greatest Decrease in Profits: " + greatest_decrease['date'] + " ($" + str(int(greatest_decrease['amount'])) + ")")

output_text = "\n".join(output)

print(output_text)

with open("financial_analysis.txt", "w") as text_file:
    text_file.write(output_text)