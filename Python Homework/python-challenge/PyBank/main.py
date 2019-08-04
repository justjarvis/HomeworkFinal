import csv
import os

load_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("finance_analytics.txt")

total_of_months = 0
change_month = []
average_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_money = 0



with open(load_file) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    first_row = next(reader)
    total_of_months = total_of_months + 1
    total_money = total_money + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        total_of_months = total_of_months + 1
        total_money = total_money + int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        average_change = average_change + [net_change]
        change_month = change_month + [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

monthly_average_change = float(sum(average_change) / len(average_change))



output = (
    f"\nFinancial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {total_of_months}\n"
    f"Total: ${total_money}\n"
    f"Average Change: ${monthly_average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease}\n")

print(output)

with open(output_file, "w") as txt_file:
    txt_file.write(output)