monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_saving = monthly_income - monthly_expenses
projected_savings = int(monthly_saving * 12 + (monthly_saving * 12 * 0.05))

print(f"Your monthly savings are ${monthly_saving}.\nProjected savings after one year, with interest, is: ${projected_savings}")