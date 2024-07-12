import os
import csv

budget = os.path.join("Resources", "budget_data.csv")

with open(budget, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    total_months = 0
    for row in csv_reader:
        total_months += 1

print("The total number of months = " + str(total_months))
