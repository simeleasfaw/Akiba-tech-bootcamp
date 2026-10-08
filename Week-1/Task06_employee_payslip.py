Employee_name = input("Enter employee name: ")
Basic_salary = float(input("Enter basic salary: "))
Transport_allowance = float(input("Enter transport allowance: "))
Food_allowance = float(input("Enter food allowance: "))

Gross_Salary = Basic_salary + Transport_allowance + Food_allowance

print("==========================================")
print("           EMPLOYEE PAYSLIP               ")
print("==========================================")
print(f"\nEmployee: {Employee_name}")
print(f"{'Basic salary:':<25}{Basic_salary:>12,.2f} ETB") 
print(f"{'Transport Allowance:':<25}{Transport_allowance:>12,.2f} ETB")
print(f"{'Food Allowance:':<25}{Food_allowance:>12,.2f} ETB")
print("-" * 40)
print(f"{'Gross Salary:':<25}{Gross_Salary:>12,.2f} ETB")

